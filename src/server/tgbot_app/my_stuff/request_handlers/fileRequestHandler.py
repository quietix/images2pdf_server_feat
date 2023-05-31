from src.server.setupConfig import bot
from .requestHandler import RequestHandler
from src.server.tgbot_app.my_stuff.msgs.fileMsg import FileMsg
import os


class FileRequestHandler(RequestHandler):
    def handle_request(self, msg: FileMsg):
        chat_id = msg.chat_id
        file_name = msg.file_name
        file_id = msg.file_id

        # TODO downloading via fileManager
        file_path = f'downloads/{file_name}'
        bot.download_file(file_id, file_path)
        bot.sendDocument(chat_id, open(file_path, 'rb'))
        os.remove(file_path)