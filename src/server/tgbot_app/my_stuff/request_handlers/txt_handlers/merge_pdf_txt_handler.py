from .abstract_txt_handler import AbstractTxtRequestHandler
from ...msgs.txtMsg import TxtMsg
import time
from src.server.tgbot_app.my_stuff.factories.interaction_stuff_factories.merge_pdf_factory import MergePdfFactory


class MergePdfTxtHandler(AbstractTxtRequestHandler):
    mergePdfFactory = MergePdfFactory()
    _response = mergePdfFactory.get_response()


    def __init__(self, response = mergePdfFactory.get_response(), file_manager = mergePdfFactory.get_file_manager()):
        self._response = response
        self._file_manager = file_manager


    def get_file_manager(self):
        return self._file_manager


    def get_response(self):
        return self._response


    def handle_request(self, msg: TxtMsg):
        if msg.text == "/merge_pdf":
            self._response.response_with_reply_keyboard_when_opening_merge_session(msg.chat_id)

        elif msg.text == "Об'єднати pdf 📂":
            user_dir_composite = self._file_manager.download_pdfs(msg.user_id)
            if len(user_dir_composite.children) == 0:
                self._response.response_with_reply_keyboard_when_waiting_pdfs_state_2(msg.chat_id)
                user_dir_composite.delete_self()
            else:
                self._response.response_with_reply_keyboard_when_received_pdfs(msg.chat_id)

        elif msg.text == "Відмінити об'єднання pdf ❌":
            self._response.delete_reply_keyboard(msg.chat_id, "Сеанс об'єднання pdf завершено.")
            self._file_manager.delete_directory(msg.user_id)

        elif msg.text == "Автоматична назва 📂":
            self._response.send_message(msg.chat_id, 'Створюється pdf...')
            user_dir_composite = self._file_manager.create_pdf_paths_list(msg.user_id)
            auto_file_name: str = str(msg.user_id) + '-' + str(time.strftime("%Y%m%d-%H%M%S"))
            pdf_path = self._file_manager.create_pdf_from_pdf_list(user_dir_composite, auto_file_name)
            self._response.send_document(msg.chat_id, document=open(pdf_path, 'rb'))
            self._file_manager.delete_directory(msg.user_id)
            self._response.response_with_reply_keyboard_when_pdf_is_sent_merge(msg.chat_id)

        elif msg.text == "Продовжити об'єднання 📂":
            self._response.response_with_reply_keyboard_when_merge_session_was_continued(msg.chat_id)

        elif msg.text == "Моя назва 📂":
            self._response.delete_reply_keyboard(msg.chat_id, "Введіть назву pdf. Коли буде кінцевий варіант, натисніть /ready_merge")

        elif msg.text == "/ready_merge":
            self._response.send_message(msg.chat_id, 'Створюється pdf...')
            user_dir_composite = self._file_manager.create_pdf_paths_list(msg.user_id)
            file_name = self._file_manager.get_last_non_command_message_text(msg.user_id)
            pdf_path = self._file_manager.create_pdf_from_pdf_list(user_dir_composite, file_name)
            self._response.send_document(msg.chat_id, document=open(pdf_path, 'rb'))
            self._file_manager.delete_directory(msg.user_id)
            self._response.response_with_reply_keyboard_when_pdf_is_sent_creation(msg.chat_id)

        else:
            super().handle_request(msg)