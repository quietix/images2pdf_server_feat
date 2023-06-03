from src.server.setupConfig import bot
from .requestHandler import RequestHandler
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
from ..response import Response
from ..file_manager.local_file_manager import LocalFileManager
from ..controllers.pdf_creation_controllers.pdf_creator_proxy import PdfCreatorProxy
import time


class TxtRequestHandler(RequestHandler):
    def handle_request(self, msg: TxtMsg):
        user_id = msg.user_id
        msg_text = msg.text
        chat_id = msg.chat_id
        pdfCreator = PdfCreatorProxy(chat_id, user_id)

        if msg_text == '/start':
            Response.send_message(chat_id, "Вітаю")

        elif msg_text == '/help':
            Response.send_message(chat_id, "Натисніть /create_pdf та дотримуйтесь вказівок.")

        elif msg_text == '/create_pdf':
            pdfCreator.open_session()

        elif msg_text == "Створити pdf":
            pdfCreator.invoke_creation()

        elif msg_text == "Відмінити створення pdf":
            pdfCreator.cancel_creation()

        elif msg_text == "Автоматична назва":
            pdfCreator.create_with_auto_name()

        elif msg_text == "Продовжити створення":
            pdfCreator.continue_creation()

        elif msg_text == "Завершити сеанс":
            pdfCreator.end_session()

        elif msg_text == "Моя назва":
            pdfCreator.prepare_custom_name()

        elif msg_text == "/ready":
            pdfCreator.create_with_custom_name()