import json
import os

# Step 1: Define target JSON file
script_directory = os.path.dirname(os.path.abspath(__file__))
data_directory_raw = os.path.join(script_directory, '..', 'data', 'raw')
data_directory_manipulated = os.path.join(script_directory, '..', 'data', 'manipulated')
input_name = input("Enter the name of the input JSON file: ")
# Format user input correctly
if input_name.lower().endswith('.json'):
    # Input_name remains the same
    input_file = os.path.join(data_directory_raw, input_name)
elif '.' not in input_name:
    # No file extension add .json to the input_name
    input_name += '.json'
    input_file = os.path.join(data_directory_raw, input_name)
else:
    # Likely incorrect input of file extension, remove everything after '.', replace with .json
    input_name = input_name[:input_name.rindex('.')]
    input_name += '.json'
    input_file = os.path.join(data_directory_raw, input_name)

# Read the target JSON file
with open(input_file) as fi:
    data = json.load(fi)

# Display existing fields
existing_fields = list(data[0].keys())
print("Existing fields in the provided JSON file:")
for field in existing_fields:
    print(field)

# Step 2: Selected fields to drop
fields_to_drop = []
while len(fields_to_drop) == 0 or len(fields_to_drop) == len(existing_fields):
    fields_to_drop = input("Enter the fields to drop (comma-separated): ").split(",")
    fields_to_drop = [field.strip().lower() for field in fields_to_drop]

    # Check if all fields are present and prevent dropping all fields
    for field in fields_to_drop:
        if field not in existing_fields:
            print(f"Field '{field}' does not exist in the JSON file. Please try again.")
            fields_to_drop = []
            break

    if len(fields_to_drop) == len(existing_fields):
        print("Cannot drop all fields. Please try again.")

# Drop fields from each object
new_data = []
for obj in data:
    new_obj = {k: v for k, v in obj.items() if k.lower() not in fields_to_drop}
    new_data.append(new_obj)

# Generate the output file name based on input file name
file_name, file_ext = os.path.splitext(input_name)
output_location = os.path.join(data_directory_manipulated, f"{file_name}_altered{file_ext}")

# Check for existing files with matching file name and increment counter
counter = 1
while os.path.exists(output_location):
    output_location = os.path.join(data_directory_manipulated, f"{file_name}_altered{counter}{file_ext}")
    counter += 1

# Write the updated JSON data to the output file
with open(output_location, 'w') as fo:
    json.dump(new_data, fo, indent=4)

print("Fields dropped:", fields_to_drop)
print("Altered JSON file saved as", output_location)
