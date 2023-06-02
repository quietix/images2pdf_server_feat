from abc import ABC, abstractmethod


class FileManager(ABC):
    @staticmethod
    @abstractmethod
    def record_request(request_body):
        pass

    @staticmethod
    @abstractmethod
    def download_photo(user_id):
        pass