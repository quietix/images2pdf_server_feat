from src.server.tgbot_app.my_stuff.request_handlers.requestHandler import RequestHandler
from src.server.tgbot_app.my_stuff.request_handlers.imgRequestHandler import ImgRequestHandler
from src.server.tgbot_app.my_stuff.request_handlers.txtRequestHandler import TxtRequestHandler
from src.server.tgbot_app.my_stuff.request_handlers.fileRequestHandler import FileRequestHandler
from src.server.tgbot_app.my_stuff.request_handlers.notCreatedRequestHandler import NotCreatedRequestHandler

from src.server.tgbot_app.my_stuff.msgs.msg import Msg
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
from src.server.tgbot_app.my_stuff.msgs.imgMsg import ImgMsg
from src.server.tgbot_app.my_stuff.msgs.fileMsg import FileMsg


class Handler_Creator:

    # Factory method
    @staticmethod
    def create_handler(msg: Msg) -> RequestHandler:
        if isinstance(msg, TxtMsg):
            return TxtRequestHandler()
        elif isinstance(msg, ImgMsg):
            return ImgRequestHandler()
        elif isinstance(msg, FileMsg):
            return FileRequestHandler()
        return NotCreatedRequestHandler()