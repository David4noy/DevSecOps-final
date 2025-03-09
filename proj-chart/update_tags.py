#!/usr/bin/env python3
import sys
import yaml

# Constant for the YAML file path (assumes it's in the same folder)
VALUES_FILE = "values.yaml"

def update_tags(flask_tag, python_tag):
    # Load the YAML file
    with open(VALUES_FILE, 'r') as f:
        data = yaml.safe_load(f)
    
    # Update the tag values
    data['flaskApp']['tag'] = flask_tag
    data['pythonServer']['tag'] = python_tag
    
    # Write the changes back to the file
    with open(VALUES_FILE, 'w') as f:
        yaml.safe_dump(data, f, default_flow_style=False)
    print(f"Updated tags in {VALUES_FILE}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <new_flask_tag> <new_python_tag>".format(sys.argv[0]))
        sys.exit(1)
    
    new_flask_tag = sys.argv[1]
    new_python_tag = sys.argv[2]
    
    update_tags(VALUES_FILE, new_flask_tag, new_python_tag)
