import json
import os

# Step 1: Define target JSON file
script_directory = os.path.dirname(os.path.abspath(__file__))
data_directory_raw = os.path.join(script_directory, '..', 'data', 'raw')
data_directory_manipulated = os.path.join(script_directory, '..', 'data', 'manipulated')
input_file = input("Enter the name of the input JSON file: ")

# Get user input for host_id range
host_id_lower = int(input("Enter the lower value of host_id: "))
host_id_upper = int(input("Enter the upper value of host_id: "))

# Toggle the status field for host_id within the se range
for obj in data_directory_raw:
    host_id = obj['host_id']
    if host_id_lower <= host_id <= host_id_upper:
        if obj['status'] == "fail":
            obj['status'] = "pass"
        elif obj['status'] == "pass":
            obj['status'] = "fail"

# Create and write output file with desired JSON format
output_file = input_file[:-5] + "_alteredData.json"
with open(output_file, 'w') as f:
    json.dump(data_directory_manipulated, f, indent=4)

print("Status updated for host_id range", host_id_lower, "to", host_id_upper)
print("Changes saved to", output_file)

