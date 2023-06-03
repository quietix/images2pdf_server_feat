from .pdf_creator import PdfCreator
from ...response import Response
from ...file_manager.local_file_manager import LocalFileManager
from src.server.setupConfig import bot
import time


# Facade (hiding system complexity behind simple interface)
class StandardPdfCreator(PdfCreator):

    def __init__(self, chat_id, user_id):
        super().__init__(chat_id, user_id)

    def open_session(self):
        Response.response_with_reply_keyboard_when_waiting_photos(self.chat_id)

    def invoke_creation(self):
        Response.response_with_reply_keyboard_when_received_photos(self.chat_id)

    def cancel_creation(self):
        Response.delete_reply_keyboard(self.chat_id, 'Сеанс створення pdf завершено.')
        LocalFileManager.delete_directory(self.user_id)

    def create_with_auto_name(self):
        Response.send_message(self.chat_id, 'Створюється pdf...')
        photo_list = LocalFileManager.create_photo_list_from_existing_files_in_directory(self.user_id)
        auto_file_name: str = str(self.user_id) + '-' + str(time.strftime("%Y%m%d-%H%M%S"))
        pdf_path = LocalFileManager.create_pdf_from_photo_list(self.user_id, photo_list, auto_file_name)
        bot.sendDocument(self.chat_id, document=open(pdf_path, 'rb'))
        LocalFileManager.delete_directory(self.user_id)
        Response.response_with_reply_keyboard_when_pdf_is_sent(self.chat_id)

    def continue_creation(self):
        Response.response_with_reply_keyboard_when_session_was_continued(self.chat_id)

    def end_session(self):
        Response.delete_reply_keyboard(self.chat_id, "Сеанс створення pdf завершено.")

    def prepare_custom_name(self):
        Response.delete_reply_keyboard(self.chat_id, "Введіть назву pdf. Коли буде кінцевий варіант, натисніть /ready")

    def create_with_custom_name(self):
        Response.send_message(self.chat_id, 'Створюється pdf...')
        photo_list = LocalFileManager.create_photo_list_from_existing_files_in_directory(self.user_id)
        file_name = LocalFileManager.get_last_non_command_message_text(self.user_id)
        pdf_path = LocalFileManager.create_pdf_from_photo_list(self.user_id, photo_list, file_name)
        bot.sendDocument(self.chat_id, document=open(pdf_path, 'rb'))
        LocalFileManager.delete_directory(self.user_id)
        Response.response_with_reply_keyboard_when_pdf_is_sent(self.chat_id)