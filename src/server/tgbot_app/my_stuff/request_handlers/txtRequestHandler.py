from src.server.setupConfig import bot
from .requestHandler import RequestHandler
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
from ..response import Response
from ..file_manager.local_file_manager import LocalFileManager
import time


class TxtRequestHandler(RequestHandler):
    def handle_request(self, msg: TxtMsg):
        user_id = msg.user_id
        msg_text = msg.text
        chat_id = msg.chat_id

        if msg_text == '/start':
            Response.send_message(chat_id, "Вітаю")

        elif msg_text == '/help':
            Response.send_message(chat_id, "Натисніть /create_pdf та дотримуйтесь вказівок.")

        elif msg_text == '/create_pdf':
            Response.response_with_reply_keyboard_when_waiting_photos(chat_id)

        elif msg_text == "Створити pdf":
            photo_list = LocalFileManager.download_photo(user_id)
            if len(photo_list) <= 0:
                Response.response_with_reply_keyboard_when_waiting_photos_state_2(chat_id)
            else:
                Response.response_with_reply_keyboard_when_received_photos(chat_id)

        elif msg_text == "Відмінити створення pdf":
            Response.delete_reply_keyboard(chat_id, 'Сеанс створення pdf завершено.')
            LocalFileManager.delete_directory(user_id)

        elif msg_text == "Автоматична назва":
            Response.send_message(chat_id, 'Створюється pdf...')
            photo_list = LocalFileManager.create_photo_list_from_existing_files_in_directory(user_id)
            auto_file_name: str = (str)(user_id) + '-' + (str)(time.strftime("%Y%m%d-%H%M%S"))
            pdf_path = LocalFileManager.create_pdf_from_photo_list(user_id, photo_list, auto_file_name)
            bot.sendDocument(chat_id, document=open(pdf_path, 'rb'))

            LocalFileManager.delete_directory(user_id)

            Response.response_with_reply_keyboard_when_pdf_is_sent(chat_id)

        elif msg_text == "Продовжити створення":
            Response.response_with_reply_keyboard_when_session_was_continued(chat_id)

        elif msg_text == "Завершити сеанс":
            Response.delete_reply_keyboard(chat_id, "Сеанс створення pdf завершено.")

        elif msg_text == "Моя назва":
            Response.delete_reply_keyboard(chat_id, "Введіть назву pdf. Коли буде кінцевий варіант, натисніть /ready")

        elif msg_text == "/ready":
            Response.send_message(chat_id, 'Створюється pdf...')
            photo_list = LocalFileManager.create_photo_list_from_existing_files_in_directory(user_id)
            file_name = LocalFileManager.get_last_non_command_message_text(user_id)
            pdf_path = LocalFileManager.create_pdf_from_photo_list(user_id, photo_list, file_name)
            bot.sendDocument(chat_id, document=open(pdf_path, 'rb'))

            LocalFileManager.delete_directory(user_id)

            Response.response_with_reply_keyboard_when_pdf_is_sent(chat_id)