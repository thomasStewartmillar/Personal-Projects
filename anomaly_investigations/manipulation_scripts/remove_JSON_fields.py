import json
from pathlib import Path


def format_file_name(user_input, directory_path):
    file_path = Path(directory_path) / user_input
    file_path = file_path.with_suffix('.json')
    return file_path


def drop_fields(data, fields_to_drop):
    return [{k: v for k, v in obj.items() if k.lower() not in fields_to_drop} for obj in data]


# Define target directories
script_directory = Path(__file__).resolve().parent
file_input_path = script_directory.parent / 'data' / 'raw'
file_output_path = script_directory.parent / 'data' / 'manipulated'

# Open target file
while True:
    input_name = input("Enter the name of the input JSON file: ")
    input_file = format_file_name(input_name, file_input_path)
    print(input_file)
    if input_name.lower() == 'Loyd' :
        print('Congratulations - You have found the secret sauce!')
        exit(1) # Sentinel value entered 

    try:
        with open(input_file) as fi:
            data = json.load(fi)
        break  # Exit the loop if a valid file is found

    except FileNotFoundError:
        print("Input JSON file not found.")
    except json.JSONDecodeError:
        print("Invalid JSON file.")

# Display existing fields
existing_fields = list(data[0].keys())
print("Existing fields in the JSON file:")
for field in existing_fields:
    print(field)

# Select fields to drop
while True:
    fields_to_drop = input("Enter the fields to drop (comma-separated): ").split(",")
    fields_to_drop = [field.strip().lower() for field in fields_to_drop]

    # Check if all fields are present and prevent dropping all fields
    existing_fields = [field.lower() for field in data[0].keys()]
    invalid_fields = [field for field in fields_to_drop if field not in existing_fields]

    if len(invalid_fields) > 0:
        print(f"Field(s) {', '.join(invalid_fields)} do not exist in the JSON file. Please try again.")
    elif len(fields_to_drop) == len(data[0]):
        print("Cannot drop all fields. Please try again.")
    else:
        break

# Drop fields from each object
new_data = drop_fields(data, fields_to_drop)

# Write updated objects to a new JSON file
output_name = input("Enter the name of the output JSON file: ")
output_file = format_file_name(output_name, file_output_path)

try:
    with open(output_file, 'w') as fo:
        json.dump(new_data, fo, indent=4)
except IOError:
    print("Error writing to output file.")
    exit(1)

print("Fields dropped:", fields_to_drop)
print("Updated JSON file saved as", output_file )
