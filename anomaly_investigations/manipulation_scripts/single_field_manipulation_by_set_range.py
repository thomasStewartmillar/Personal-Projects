import json

# Read JSON file
input_file = input("Enter the name of the input JSON file: ")
with open(input_file) as f:
    data = json.load(f)

# Get user input for host_id range
host_id_lower = int(input("Enter the lower value of host_id: "))
host_id_upper = int(input("Enter the upper value of host_id: "))

# Toggle the status field for host_id within the range
for obj in data:
    host_id = obj['host_id']
    if host_id_lower <= host_id <= host_id_upper:
        if obj['status'] == "fail":
            obj['status'] = "pass"
        elif obj['status'] == "pass":
            obj['status'] = "fail"

# Create output_file name in desired format
output_file = input_file[:-5] + "_altered.json"

# Write the changes to the output JSON file
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print("Status updated for host_id range", host_id_lower, "to", host_id_upper)
print("Changes saved to", output_file)

