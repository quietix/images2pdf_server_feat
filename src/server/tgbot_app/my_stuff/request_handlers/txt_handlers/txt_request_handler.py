from __future__ import annotations

from src.server.tgbot_app.my_stuff.request_handlers.request_handler import RequestHandler
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
from abc import abstractmethod


class TxtRequestHandler(RequestHandler):

    @abstractmethod
    def set_next(self, txt_handler: TxtRequestHandler):
        pass

    @abstractmethod
    def handle_request(self, msg: TxtMsg):
        pass