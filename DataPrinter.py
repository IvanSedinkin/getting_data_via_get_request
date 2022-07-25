import csv

import jsonpickle
import os
import pandas

class DataPrinter:
    def __init__(self, json_object: jsonpickle.json, path: str, file_name: str):
        self.json_object = json_object
        self.path = path
        self.file_name = file_name

    def write_to_csv(self):
        with open(self.path + f"/{self.file_name}", "w") as file:
            writer = csv.writer(file)
            writer.writerow(self.json_object.values())
