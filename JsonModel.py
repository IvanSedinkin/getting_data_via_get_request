import jsonpickle as jp


class JsonModel:
    def __init__(self, json_string: jp.json):
        print(json_string)
        _string = json_string
        self.user_id = _string['userId']
        self.id = _string['id']
        self.title = _string['title']
        self.completed = _string['completed']
