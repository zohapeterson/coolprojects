import json
import os

## Correct File Path
wd = r'C://Users//zohap//OneDrive//Documents//github//coolprojects//notebook'
file_path = os.path.join(wd, "notebook_data.json")

## Vars
new_data = {2: "JSON Test 2"}

## Open and Read from JSON file
with open(file_path, 'r') as file:
    old_data = json.load(file)
    print(old_data)

## Dump new data to JSON file
with open(file_path, 'w') as file:
    json.dump(new_data, file)
