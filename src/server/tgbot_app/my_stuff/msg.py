from abc import ABC
from src.server.tgbot_app.my_stuff.exceptions import TxtMsgNotCreated


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


class TxtMsg(Msg):
    text: str

    def __init__(self, request_body: dict):
        Msg.__init__(self, request_body)
        try:
            self.text = request_body['message']['text']
        except TxtMsgNotCreated as e:
            print(e)

    @staticmethod
    def can_be_created(request_body: dict):
        if 'message' in request_body:
            if 'text' in request_body['message']:
                return True
        return False


class ImgMsg(Msg):
    file_id: int

    def __init__(self, request_body: dict):
        Msg.__init__(self, request_body)
        try:
            self.file_id = request_body['message']['photo'][len(request_body['message']['photo']) - 1]['file_id']
        except TxtMsgNotCreated as e:
            print(e)

    @staticmethod
    def can_be_created(request_body: dict):
        if 'message' in request_body:
            if 'photo' in request_body['message']:
                return True
        return False


# TODO FileMsg