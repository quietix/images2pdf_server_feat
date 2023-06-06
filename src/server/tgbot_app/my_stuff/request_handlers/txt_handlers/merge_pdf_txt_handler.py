from .abstract_txt_handler import AbstractTxtRequestHandler
from ...msgs.txtMsg import TxtMsg
import time
from src.server.tgbot_app.my_stuff.factories.interaction_stuff_factories.merge_pdf_factory import MergePdfFactory


class MergePdfTxtHandler(AbstractTxtRequestHandler):

    def __init__(self):
        mergePdfFactory = MergePdfFactory()
        self._response = mergePdfFactory.get_response()
        self._file_manager = mergePdfFactory.get_file_manager()

    def handle_request(self, msg: TxtMsg):
        if msg.text == "/merge_pdf":
            self._response.response_with_reply_keyboard_when_opening_merge_session(msg.chat_id)

        elif msg.text == "Об'єднати pdf 📂":
            pdf_list = self._file_manager.download_pdfs(msg.user_id)
            if len(pdf_list) <= 0:
                self._response.response_with_reply_keyboard_when_waiting_pdfs_state_2(msg.chat_id)
            else:
                self._response.response_with_reply_keyboard_when_received_pdfs(msg.chat_id)

        elif msg.text == "Відмінити об'єднання pdf ❌":
            self._response.delete_reply_keyboard(msg.chat_id, "Сеанс об'єднання pdf завершено.")
            self._file_manager.delete_directory(msg.user_id)

        elif msg.text == "Автоматична назва 📂":
            self._response.send_message(msg.chat_id, 'Створюється pdf...')
            pdf_list = self._file_manager.create_pdf_paths_list(msg.user_id)
            auto_file_name: str = str(msg.user_id) + '-' + str(time.strftime("%Y%m%d-%H%M%S"))
            pdf_path = self._file_manager.create_pdf_from_pdf_list(msg.user_id, pdf_list, auto_file_name)
            self._response.send_document(msg.chat_id, document=open(pdf_path, 'rb'))
            self._file_manager.delete_directory(msg.user_id)
            self._response.response_with_reply_keyboard_when_pdf_is_sent_merge(msg.chat_id)

        elif msg.text == "Продовжити об'єднання 📂":
            self._response.response_with_reply_keyboard_when_merge_session_was_continued(msg.chat_id)

        elif msg.text == "Моя назва 📂":
            self._response.delete_reply_keyboard(msg.chat_id, "Введіть назву pdf. Коли буде кінцевий варіант, натисніть /ready_merge")

        elif msg.text == "/ready_merge":
            self._response.send_message(msg.chat_id, 'Створюється pdf...')
            pdf_list = self._file_manager.create_pdf_paths_list(msg.user_id)
            file_name = self._file_manager.get_last_non_command_message_text(msg.user_id)
            pdf_path = self._file_manager.create_pdf_from_pdf_list(msg.user_id, pdf_list, file_name)
            self._response.send_document(msg.chat_id, document=open(pdf_path, 'rb'))
            self._file_manager.delete_directory(msg.user_id)
            self._response.response_with_reply_keyboard_when_pdf_is_sent_creation(msg.chat_id)

        else:
            super().handle_request(msg)