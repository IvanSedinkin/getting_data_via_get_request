import requests
import jsonpickle


class DataProcessor:
    def __init__(self, api_url, number) -> jsonpickle.json:
        self.api_url = api_url
        self.number = str(number)

    def get_answer(self):
        response = requests.get(self.api_url + "/" + self.number).json()
        return response
