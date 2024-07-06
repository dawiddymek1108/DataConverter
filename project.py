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
import sys
import json
import xml.etree.ElementTree as ET
import yaml
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel

class ConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.input_file = None
        self.output_file = None

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel('Select files for conversion', self)
        layout.addWidget(self.label)

        self.btn_open = QPushButton('Open Input File', self)
        self.btn_open.clicked.connect(self.openFileDialog)
        layout.addWidget(self.btn_open)

        self.btn_save = QPushButton('Save Output File', self)
        self.btn_save.clicked.connect(self.saveFileDialog)
        layout.addWidget(self.btn_save)

        self.btn_convert = QPushButton('Convert', self)
        self.btn_convert.clicked.connect(self.convertData)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)
        self.setWindowTitle('Data Converter')
        self.show()

    def openFileDialog(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Open Input File", "", "All Files (*);;JSON Files (*.json);;XML Files (*.xml);;YAML Files (*.yml *.yaml)", options=options)
        if file:
            self.input_file = file
            self.label.setText(f'Input file: {file}')

    def saveFileDialog(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getSaveFileName(self, "Save Output File", "", "All Files (*);;JSON Files (*.json);;XML Files (*.xml);;YAML Files (*.yml *.yaml)", options=options)
        if file:
            self.output_file = file
            self.label.setText(f'Output file: {file}')

    def convertData(self):
        if not self.input_file or not self.output_file:
            self.label.setText('Please select both input and output files')
            return

        data = None
        if self.input_file.endswith('.json'):
            data = self.load_json(self.input_file)
        elif self.input_file.endswith('.xml'):
            data = self.load_xml(self.input_file)
        elif self.input_file.endswith('.yml') or self.input_file.endswith('.yaml'):
            data = self.load_yaml(self.input_file)
        else:
            self.label.setText('Unsupported input file format')
            return

        if self.output_file.endswith('.json'):
            self.save_json(data, self.output_file)
        elif self.output_file.endswith('.xml'):
            self.save_xml(data, self.output_file)
        elif self.output_file.endswith('.yml') or self.output_file.endswith('.yaml'):
            self.save_yaml(data, self.output_file)
        else:
            self.label.setText('Unsupported output file format')
            return

        self.label.setText(f'Converted {self.input_file} to {self.output_file}')

    def load_json(self, file_path):
        with open(file_path, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                self.label.setText("Invalid JSON format")

    def save_json(self, data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def load_xml(self, file_path):
        try:
            tree = ET.parse(file_path)
            return tree.getroot()
        except ET.ParseError:
            self.label.setText("Invalid XML format")

    def save_xml(self, data, file_path):
        tree = ET.ElementTree(data)
        tree.write(file_path)

    def load_yaml(self, file_path):
        with open(file_path, 'r') as file:
            try:
                return yaml.safe_load(file)
            except yaml.YAMLError:
                self.label.setText("Invalid YAML format")

    def save_yaml(self, data, file_path):
        with open(file_path, 'w') as file:
            yaml.safe_dump(data, file)

def main():
    app = QApplication(sys.argv)
    ex = ConverterUI()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    