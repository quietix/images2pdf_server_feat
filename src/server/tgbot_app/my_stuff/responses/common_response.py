from src.server.tgbot_app.my_stuff.responses.base_response import BaseResponse
from telepot.namedtuple import ReplyKeyboardRemove
import telepot
import dotenv

bot = telepot.Bot(dotenv.dotenv_values('.env')['TOKEN'])


class CommonResponse(BaseResponse):

    def send_message(self, chat_id, text):
        bot.sendMessage(chat_id, text)

    def send_document(self, chat_id, document):
        bot.sendDocument(chat_id, document)

    def download_file(self, file_id, file_path):
        bot.download_file(file_id, file_path)

    def delete_reply_keyboard(self, chat_id, text):
        bot.sendMessage(chat_id, text, reply_markup=ReplyKeyboardRemove())