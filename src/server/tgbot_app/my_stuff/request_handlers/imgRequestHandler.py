from src.server.setupConfig import bot
from .requestHandler import RequestHandler
from src.server.tgbot_app.my_stuff.msgs.imgMsg import ImgMsg
import os


class ImgRequestHandler(RequestHandler):
    def handle_request(self, msg: ImgMsg):
        file_id = msg.file_id

        # TODO downloading via fileManager
        photo_path = f'downloads/{file_id}.jpg'
        bot.download_file(file_id, photo_path)
        bot.sendPhoto(msg.chat_id, open(photo_path, 'rb'))
        os.remove(photo_path)