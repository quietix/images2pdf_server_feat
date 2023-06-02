from src.server.tgbot_app.my_stuff.msgs.msg import Msg
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
from src.server.tgbot_app.my_stuff.msgs.imgMsg import ImgMsg
from src.server.tgbot_app.my_stuff.msgs.fileMsg import FileMsg


class Msg_Creator:

    # Factory method
    @staticmethod
    def create_msg(request_body) -> Msg:
        if TxtMsg.can_be_created(request_body):
            return TxtMsg(request_body)
        elif ImgMsg.can_be_created(request_body):
            return ImgMsg(request_body)
        elif FileMsg.can_be_created(request_body):
            return FileMsg(request_body)
        return Msg(request_body)
