from abc import ABC, abstractmethod


class BaseFile(ABC):

    path: str = None

    def __init__(self, path):
        """Downloads the file into <user_id/> folder"""
        self.path = path

    @abstractmethod
    def delete_self(self):
        pass

    @abstractmethod
    def print_path(self):
        pass