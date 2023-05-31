from src.server.tgbot_app.my_stuff.request_handlers.requestHandler import RequestHandler
from src.server.tgbot_app.my_stuff.msgs.msg import Msg


# Context
class Handlers_Controller:
    __msg: Msg
    # Strategy
    __handler: RequestHandler

    def __init__(self, msg: Msg, handler: RequestHandler):
        self.__msg = msg
        self.__handler = handler

    def handle_request(self):
        self.__handler.handle_request(self.__msg)