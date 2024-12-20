import json
import csv

class DataStorage:
    def __init__(self, filename):
        self.filename = filename

    def save_to_json(self, data):
        with open(self.filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def save_to_csv(self, data):
        with open(self.filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data[0].keys())  # Write header
            for item in data:
                writer.writerow(item.values())  # Write data rows

    def load_from_json(self):
        with open(self.filename, 'r') as json_file:
            return json.load(json_file)

    def load_from_csv(self):
        with open(self.filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            return [row for row in reader]