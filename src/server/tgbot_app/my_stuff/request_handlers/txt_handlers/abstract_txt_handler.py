from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
from src.server.tgbot_app.my_stuff.request_handlers.txt_handlers.txt_request_handler import TxtRequestHandler
from abc import abstractmethod


# Chain of responsibility
class AbstractTxtRequestHandler(TxtRequestHandler):

    _next_txt_handler: TxtRequestHandler = None

    def set_next(self, txt_handler: TxtRequestHandler) -> TxtRequestHandler:
        self._next_txt_handler = txt_handler
        return txt_handler

    @abstractmethod
    def handle_request(self, msg: TxtMsg):
        if self._next_txt_handler:
            self._next_txt_handler.handle_request(msg)