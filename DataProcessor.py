import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
from JsonModel import JsonModel


class DataProcessor:
    def __init__(self, api_url, number):
        self.api_url = api_url
        self.number = str(number)

    def get_answer(self):
        response = requests.get(self.api_url + "/" + self.number).json()
        return response
