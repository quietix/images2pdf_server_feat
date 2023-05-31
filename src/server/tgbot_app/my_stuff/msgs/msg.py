from abc import ABC


class Msg(ABC):
    update_id: int
    chat_id: int
    first_name: str
    username: str

    def __init__(self, request_body: dict):
        self.update_id = int(request_body['update_id'])
        self.chat_id = int(request_body['message']['from']['id'])
        self.first_name = request_body['message']['from']['first_name']
        self.username = request_body['message']['from']['username']