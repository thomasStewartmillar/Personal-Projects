import json
import os

# Step 1: Define target JSON file
script_directory = os.path.dirname(os.path.abspath(__file__))
data_directory_raw = os.path.join(script_directory, '..', 'data', 'raw')
data_directory_manipulated = os.path.join(script_directory, '..', 'data', 'manipulated')
input_name = input("Enter the name of the input JSON file: ")

# # Format user input correctly
# if input_name.lower().endswith('.json'):
#     # Input_name remains the same
#     input_file = os.path.join(data_directory_raw, input_name)
# elif '.' not in input_name:
#     # No file extension add .json to the input_name
#     input_name += '.json'
#     input_file = os.path.join(data_directory_raw, input_name)
# else:
#     # Likely incorrect input of file extension, remove everything after '.', replace with .json
#     input_name = input_name[:input_name.rindex('.')]
#     input_name += '.json'
#     input_file = os.path.join(data_directory_raw, input_name)

def format_file_name(user_input, directory_path):
    # Format user input correctly
    if input_name.lower().endswith('.json'):
        # Input_name remains the same
        input_file = os.path.join(data_directory_raw, input_name)
    elif '.' not in input_name:
        # No file extension, add .json to the input_name
        input_name += '.json'
        input_file = os.path.join(data_directory_raw, input_name)
    else:
        # Likely incorrect input of file extension, remove everything after '.', replace with .json
        input_name = input_name[:input_name.rindex('.')]
        input_name += '.json'
        input_file = os.path.join(data_directory_raw, input_name)
    
    return input_file

# Read the target JSON file
input_file = format_file_name(input_name, data_directory_raw)
with open(input_file) as fi:
    data = json.load(fi)

# Display existing fields
existing_fields = list(data[0].keys())
print("Existing fields in the JSON file:")
for field in existing_fields:
    print(field)

# Step 2: Selected fields to drop
fields_to_drop = []
while len(fields_to_drop) == 0 or len(fields_to_drop) == len(data[0]):
    fields_to_drop = input("Enter the fields to drop (comma-separated): ").split(",")
    fields_to_drop = [field.strip().lower() for field in fields_to_drop]

    # Check if all fields are present and prevent dropping all fields
    existing_fields = [field.lower() for field in data[0].keys()]
    for field in fields_to_drop:
        if field not in existing_fields:
            print(f"Field '{field}' does not exist in the JSON file. Please try again.")
            fields_to_drop = []
            break

    if len(fields_to_drop) == len(data[0]):
        print("Cannot drop all fields. Please try again.")

# Drop fields from each object
new_data = []
for obj in data:
    new_obj = {k: v for k, v in obj.items() if k.lower() not in fields_to_drop}
    new_data.append(new_obj)

# Step 4: Write updated objects to a new JSON file and save
trimmed_output = input("Enter the name of the output JSON file with .json extension: ")
with open(trimmed_output, 'w') as f2:
    json.dump(new_data, f2, indent=4)

print("Fields dropped:", fields_to_drop)
print("Updated JSON file saved to", trimmed_output)