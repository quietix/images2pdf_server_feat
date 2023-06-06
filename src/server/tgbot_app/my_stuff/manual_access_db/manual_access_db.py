from abc import ABC, abstractmethod
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg


class ManualAccessDB(ABC):
    @abstractmethod
    def total_cleanup(self, msg: TxtMsg):
        pass