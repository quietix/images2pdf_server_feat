from abc import ABC, abstractmethod


class BaseResponse(ABC):
    @abstractmethod
    def send_message(self, chat_id, text):
        pass

    @abstractmethod
    def send_document(self, chat_id, document):
        pass

    @abstractmethod
    def download_file(self, file_id, file_path):
        pass

    @abstractmethod
    def delete_reply_keyboard(self, chat_id, text):
        pass