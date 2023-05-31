from .msg import Msg
from ..exceptions import ImgMsgNotCreated


class ImgMsg(Msg):
    file_id: int

    def __init__(self, request_body: dict):
        Msg.__init__(self, request_body)
        try:
            self.file_id = request_body['message']['photo'][len(request_body['message']['photo']) - 1]['file_id']
        except ImgMsgNotCreated as e:
            print(e)

    @staticmethod
    def can_be_created(request_body: dict):
        if 'message' in request_body:
            if 'photo' in request_body['message']:
                return True
        return False
