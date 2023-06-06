from abc import ABC, abstractmethod
from src.server.tgbot_app.my_stuff.file_managers.base_file_manager import BaseFileManager
from src.server.tgbot_app.my_stuff.responses.base_response import BaseResponse


# Abstract Factory
class BaseInteractionStuffFactory(ABC):

    @abstractmethod
    def get_file_manager(self) -> BaseFileManager:
        pass

    @abstractmethod
    def get_response(self) -> BaseResponse:
        pass