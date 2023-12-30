from .abstract_txt_handler import AbstractTxtRequestHandler
from ...msgs.txtMsg import TxtMsg
from src.server.tgbot_app.my_stuff.factories.interaction_stuff_factories.img_2_pdf_factory import Img2PdfFactory
import time


class Img2PdfTxtHandler(AbstractTxtRequestHandler):
    img2pdfFactory = Img2PdfFactory()
    _response = img2pdfFactory.get_response()

    def __init__(self, response = img2pdfFactory.get_response(), file_manager = img2pdfFactory.get_file_manager()):
        self._response = response
        self._file_manager = file_manager


    def get_file_manager(self):
        return self._file_manager


    def get_response(self):
        return self._response


    def handle_request(self, msg: TxtMsg):
        if msg.text == '/create_pdf':
            self._response.response_with_reply_keyboard_when_waiting_photos(msg.chat_id)

        elif msg.text == "Створити pdf 🖼":
            user_dir_composite = self._file_manager.download_photos(msg.user_id)
            if len(user_dir_composite.children) == 0:
                self._response.response_with_reply_keyboard_when_waiting_photos_state_2(msg.chat_id)
                user_dir_composite.delete_self()
            else:
                self._response.response_with_reply_keyboard_when_received_photos(msg.chat_id)

        elif msg.text == "Відмінити створення pdf ❌":
            self._response.delete_reply_keyboard(msg.chat_id, 'Сеанс створення pdf завершено.')
            self._file_manager.delete_directory(msg.user_id)

        elif msg.text == "Автоматична назва 🖼":
            self._response.send_message(msg.chat_id, 'Створюється pdf...')
            user_dir_composite = self._file_manager.create_photo_paths_list(msg.user_id)
            auto_file_name: str = str(msg.user_id) + '-' + str(time.strftime("%Y%m%d-%H%M%S"))
            pdf_path = self._file_manager.create_pdf_from_photo_list(user_dir_composite, auto_file_name)
            self._response.send_document(msg.chat_id, document=open(pdf_path, 'rb'))
            self._file_manager.delete_directory(msg.user_id)
            self._response.response_with_reply_keyboard_when_pdf_is_sent_creation(msg.chat_id)

        elif msg.text == "Продовжити створення 🖼":
            self._response.response_with_reply_keyboard_when_creation_session_was_continued(msg.chat_id)

        elif msg.text == "Завершити сеанс":
            self._response.delete_reply_keyboard(msg.chat_id, "Сеанс створення pdf завершено.")

        elif msg.text == "Моя назва 🖼":
            self._response.delete_reply_keyboard(msg.chat_id, "Введіть назву pdf. Коли буде кінцевий варіант, натисніть /ready_creation")

        elif msg.text == "/ready_creation":
            self._response.send_message(msg.chat_id, 'Створюється pdf...')
            user_dir_composite = self._file_manager.create_photo_paths_list(msg.user_id)
            file_name = self._file_manager.get_last_non_command_message_text(msg.user_id)
            pdf_path = self._file_manager.create_pdf_from_photo_list(user_dir_composite, file_name)
            self._response.send_document(msg.chat_id, document=open(pdf_path, 'rb'))
            self._file_manager.delete_directory(msg.user_id)
            self._response.response_with_reply_keyboard_when_pdf_is_sent_creation(msg.chat_id)

        else:
            super().handle_request(msg)