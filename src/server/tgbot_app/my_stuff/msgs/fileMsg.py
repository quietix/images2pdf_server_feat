from .msg import Msg
from ..exceptions import FileMsgNotCreated


class FileMsg(Msg):
    file_id: int
    file_name: str

    def __init__(self, request_body: dict):
        Msg.__init__(self, request_body)
        try:
            self.file_name = request_body['message']['document']['file_name']
            self.file_id = request_body['message']['document']['file_id']
        except FileMsgNotCreated as e:
            print(e)

    @staticmethod
    def can_be_created(request_body: dict):
        if 'message' in request_body:
            if 'document' in request_body['message']:
                return True
        return False