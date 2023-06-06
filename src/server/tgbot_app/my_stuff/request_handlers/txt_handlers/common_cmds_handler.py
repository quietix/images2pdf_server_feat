from .abstract_txt_handler import AbstractTxtRequestHandler
from ...msgs.txtMsg import TxtMsg
import dotenv
from src.server.tgbot_app.my_stuff.manual_access_db.manual_access_local_db import ManualAccessLocalDB
from src.server.tgbot_app.my_stuff.manual_access_db.proxy.manual_access_local_db_proxy import ManualAccessLocalDBProxy
from src.server.tgbot_app.my_stuff.responses.common_response import CommonResponse

import telepot
bot = telepot.Bot(dotenv.dotenv_values('.env')['TOKEN'])

class CommonCmdsHandler(AbstractTxtRequestHandler):

    _common_response = CommonResponse()

    def handle_request(self, msg: TxtMsg):
        if msg.text == '/start':
            self._common_response.send_message(msg.chat_id, "Вітаю")

        elif msg.text == '/help':
            txt = "Що можна зробити:\n\n" \
                  "1) /create_pdf - створити pdf із фото.\n\n" \
                  "2) /merge_pdf - об'єднати декілька pdf у один.\n\n" \
                  "Оберіть необхідний варіант і дотримуйтесь вказівок."
            self._common_response.send_message(msg.chat_id, txt)

        elif msg.text == dotenv.dotenv_values('.env')['DATABASE_CLEANUP']:
            db_manager = ManualAccessLocalDB()
            db_manager_proxy = ManualAccessLocalDBProxy(db_manager)
            db_manager_proxy.total_cleanup(msg)

        else:
            super().handle_request(msg)