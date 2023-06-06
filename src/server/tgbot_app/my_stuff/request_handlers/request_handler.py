from abc import ABC, abstractmethod
from src.server.tgbot_app.my_stuff.msgs.msg import Msg


class RequestHandler(ABC):

    @abstractmethod
    def handle_request(self, msg: Msg):
        pass