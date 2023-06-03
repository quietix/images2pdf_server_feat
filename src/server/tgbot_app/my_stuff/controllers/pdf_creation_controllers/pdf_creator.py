from abc import ABC, abstractmethod


class PdfCreator(ABC):

    chat_id: int
    user_id: int

    def __init__(self, chat_id, user_id):
        self.chat_id = chat_id
        self.user_id = user_id

    @abstractmethod
    def open_session(self):
        """
        When received /create_pdf
        """
        pass

    @abstractmethod
    def invoke_creation(self):
        """
        When received Створити pdf
        """
        pass

    @abstractmethod
    def cancel_creation(self):
        """
        When received Відмінити створення pdf
        """
        pass

    @abstractmethod
    def create_with_auto_name(self):
        """
        When received Автоматична назва
        """
        pass

    @abstractmethod
    def continue_creation(self):
        """
        When received Продовжити створення
        """
        pass

    @abstractmethod
    def end_session(self):
        """
        When received Завершити сеанс
        """
        pass

    @abstractmethod
    def prepare_custom_name(self):
        """
        When received Моя назва
        """
        pass

    @abstractmethod
    def create_with_custom_name(self):
        """
        When received /ready
        """
        pass