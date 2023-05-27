from src.server.tgbot_app.my_stuff.request_handlers import RequestHandler, TxtRequestHandler, \
    ImgRequestHandler, NotCreatedRequestHandler
from src.server.tgbot_app.my_stuff.msg import Msg, TxtMsg, ImgMsg


# Strategy
class Handlers_Controller:
    __msg: Msg
    __handler: RequestHandler

    def __init__(self, request_body: dict):
        self.__msg = self.create_msg(request_body)
        self.__handler = self.create_handler(self.__msg)

    def handle_request(self):
        self.__handler.handle_request(self.__msg)

    @staticmethod
    def create_msg(request_body):
        if TxtMsg.can_be_created(request_body):
            return TxtMsg(request_body)
        elif ImgMsg.can_be_created(request_body):
            return ImgMsg(request_body)
        return Msg(request_body)

    @staticmethod
    def create_handler(msg: Msg) -> RequestHandler:
        if isinstance(msg, TxtMsg):
            return TxtRequestHandler()
        elif isinstance(msg, ImgMsg):
            return ImgRequestHandler()
        return NotCreatedRequestHandler()