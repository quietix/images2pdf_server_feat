from abc import ABC, abstractmethod


class BaseFileManager(ABC):
    @staticmethod
    @abstractmethod
    def record_request(request_body):
        pass