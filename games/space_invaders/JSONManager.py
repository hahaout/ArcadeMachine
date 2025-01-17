import json

class JSONManager:
    """
    For directly accessing JSON files.
    """

    def __init__(self, handler):
        self.handler = handler

    def add_entry(self, newEntry):  # creats a list and add a json element to the list .
        """
        Adds a new dictionary entry to the JSON file (list of dictionaries).
        :param newEntry: A dictionary to add to the JSON file.
        """
        data = self.handler.read_json()
        data.append(newEntry)
        self.handler.write_json(data)

    def update_entry(
        self, key, value
    ):  # update last json elem in the list with key and value
        data = self.handler.read_json()
        elem = data[-1]
        elem[key] = value
        print(elem)
        data[-1] = elem
        self.handler.write_json(data)

    def remove_entry(self, key, value):
        """
        Removes and entry from a dictionary.
        :param key:
        :return:
        """
        data = self.handler.read_json()
        updated_data = []
        for entry in data:
            if entry.get(key) != value:
                updated_data.append(
                    entry
                )  # here we rewrite the data without the element we want to remove
        if len(data) != len(
            updated_data
        ):  # to check that the data was successfully removed
            self.handler.write_json(updated_data)
            print(f"Entry with {key}='{value}' removed.")
        else:
            print(f"No entry found with {key}='{value}'.")

    def get_entry(self, key, value):
        """
        Gets and entry from json in cache.
        :param key:
        :return:
        """
        data = self.handler.read_json()

        # Check if data is a list
        for entry in data:
            if entry.get(key) == value:
                return entry
        print(f"{key}='{value}' not found :(  ")
        return None

    # TODO: CHALLENGE04 Task01 Sort Scores using Bubble Sort
    def get_highscores(self, top_x=3):
        """Fetches and returns top x highscores using a custom sorting algorithm.
        Assumes each entry in the JSON contains 'username' and 'score' keys.

        """
        # Reading data from file
        data = self.handler.read_json()

        # Convert scores to integers where applicable
        all_score = []
        for entry in data:
            score = entry.get("score", 0)
            name = entry.get("username", 0)
            # TODO: convert scores
            all_score.append([name,int(score)])

        # TODO: Bubble Sort the data
        all_sorted_score= sorted(all_score,key= lambda x:x[1], reverse=True)
        #print(all_sorted_score)
        return all_sorted_score[:top_x]