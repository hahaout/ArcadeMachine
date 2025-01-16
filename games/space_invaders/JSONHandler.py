import json


class JSONHandler:
    """
    Handles JSON files.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.validate_json()

    def validate_json(self):
        """
        Ensures the JSON file contains a list of dictionaries.
        If not, resets the file to an empty list.
        """
        data = self.read_json()
        if not isinstance(data, list) or not all(
            isinstance(entry, dict) for entry in data
        ):
            print("Invalid JSON format. Resetting to an empty list of dictionaries.")
            self.write_json([])

    def read_json(self):
        """
        Read json from disk.
        :return:
        """
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            with open(self.file_path, "w") as file:
                json.dump([], file)
            return []

    def write_json(self, data):
        """
        Write json to disk.
        :param data:
        :return:
        """
        try:
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error writing JSON: {e}")
