from abc import ABC, abstractmethod
import os
from src.server.setupConfig import bot
from src.server.tgbot_app.my_stuff.msg import Msg, TxtMsg, ImgMsg


class RequestHandler(ABC):
    @abstractmethod
    def handle_request(self, msg: Msg):
        pass


class NotCreatedRequestHandler(RequestHandler):
    def handle_request(self, msg: Msg):
        bot.sendMessage(msg.chat_id, 'Wrong message type. Try again!')


class TxtRequestHandler(RequestHandler):
    def handle_request(self, msg: TxtMsg):
        bot.sendMessage(msg.chat_id, msg.text)


# TODO redo
class ImgRequestHandler(RequestHandler):
    def handle_request(self, msg: ImgMsg):
        file_id = msg.file_id

        # TODO downloading via fileManager
        photo_path = f'downloads/{file_id}.jpg'
        bot.download_file(file_id, photo_path)
        bot.sendPhoto(msg.chat_id, open(photo_path, 'rb'))
        os.remove(photo_path)


# class FileRequestHandler(RequestHandler):
#     def handle_request(self, request_body):
#         # TODO data_extractor dependent on data_type
#         chat_id = request_body['message']['chat']['id']
#         file_name = request_body['message']['document']['file_name']
#         file_id = request_body['message']['document']['file_id']
#         # TODO downloading via fileManager
#         file_path = f'downloads/{file_name}'
#         bot.download_file(file_id, file_path)
#         bot.sendDocument(chat_id, open(file_path, 'rb'))
#         os.remove(file_path)