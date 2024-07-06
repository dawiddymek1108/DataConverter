import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")

if __name__ == "__main__":
    main()

import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            print("Invalid JSON format")
            sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if input_file.endswith('.json'):
        data = load_json(input_file)
        print("Data loaded from JSON:", data)

    # Add similar handling for XML and YAML here

    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")

if __name__ == "__main__":
    main()

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if input_file.endswith('.json'):
        data = load_json(input_file)
        print("Data loaded from JSON:", data)

    # Add similar handling for XML and YAML here

    if output_file.endswith('.json'):
        save_json(data, output_file)
        print(f"Data saved to JSON: {output_file}")

    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")

if __name__ == "__main__":
    main()

import xml.etree.ElementTree as ET
import yaml

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError:
        print("Invalid XML format")
        sys.exit(1)

def save_xml(data, file_path):
    tree = ET.ElementTree(data)
    tree.write(file_path)

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError:
            print("Invalid YAML format")
            sys.exit(1)

def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if input_file.endswith('.json'):
        data = load_json(input_file)
    elif input_file.endswith('.xml'):
        data = load_xml(input_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = load_yaml(input_file)
    else:
        print("Unsupported input file format")
        sys.exit(1)

    if output_file.endswith('.json'):
        save_json(data, output_file)
    elif output_file.endswith('.xml'):
        save_xml(data, output_file)
    elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
        save_yaml(data, output_file)
    else:
        print("Unsupported output file format")
        sys.exit(1)

    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")

if __name__ == "__main__":
    main()
