from .msg import Msg
from ..exceptions import TxtMsgNotCreated


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