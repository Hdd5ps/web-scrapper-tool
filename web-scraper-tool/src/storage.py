import json
import csv
import os

class DataStorage:
    def __init__(self, filename):
        self.filename = filename

    def save_to_json(self, data):
        if not data:
            raise ValueError("Data to save cannot be empty")
        try:
            with open(self.filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except Exception as e:
            print(f"Error saving to JSON: {e}")

    def save_to_csv(self, data):
        if not data:
            raise ValueError("Data to save cannot be empty")
        try:
            with open(self.filename, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(data[0].keys())  # Write header
                for item in data:
                    writer.writerow(item.values())  # Write data rows
        except Exception as e:
            print(f"Error saving to CSV: {e}")

    def load_from_json(self):
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"{self.filename} does not exist")
        try:
            with open(self.filename, 'r') as json_file:
                return json.load(json_file)
        except json.JSONDecodeError as e:
            print(f"Error loading JSON: {e}")
            return None
        except Exception as e:
            print(f"Error loading from JSON: {e}")
            return None

    def load_from_csv(self):
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"{self.filename} does not exist")
        try:
            with open(self.filename, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                return [row for row in reader]
        except Exception as e:
            print(f"Error loading from CSV: {e}")
            return None
