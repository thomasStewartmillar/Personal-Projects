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

# Extract unique host_id values
host_ids = set()
for obj in data:
    host_ids.add(obj['host_id'])

# Convert host_ids set to a sorted list
host_ids_list = sorted(list(host_ids))

# Add temporary_host field to the existing list with incremented values
host_values = []
for i, host_id in enumerate(host_ids_list, start=1):
    host_values.append({
        'host_id': host_id,
        'temporary_host_id': i
    })

# Sort and print the unique host_id values and associated temporary host value
host_ids_list.sort()
print("Unique host_id values:")
for host in host_values:
    print(f"Host ID: {host['host_id']}, Temporary Host: {host['temporary_host_id']}")

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
    json.dump(data, fo, indent=4)

print("Altered JSON file saved as", output_location)