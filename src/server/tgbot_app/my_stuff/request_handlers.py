from abc import ABC, abstractmethod
import os
from src.server.setupConfig import bot
from src.server.tgbot_app.my_stuff.msg import Msg, TxtMsg


class RequestHandler(ABC):
    msg: Msg  # TODO logic with this

    @abstractmethod
    def handle_request(self, request_body):
        pass


class TxtRequestHandler(RequestHandler):
    def handle_request(self, request_body):
        # TODO data_extractor dependent on data_type
        msg = TxtMsg(request_body)
        bot.sendMessage(msg.chat_id, msg.text)


class ImgRequestHandler(RequestHandler):
    def handle_request(self, request_body):
        # TODO data_extractor dependent on data_type
        chat_id = request_body['message']['chat']['id']
        file_id = request_body['message']['photo'][len(request_body['message']['photo']) - 1]['file_id']
        # TODO downloading via fileManager
        photo_path = f'downloads/{file_id}.jpg'
        bot.download_file(file_id, photo_path)
        bot.sendPhoto(chat_id, open(photo_path, 'rb'))
        os.remove(photo_path)


class FileRequestHandler(RequestHandler):
    def handle_request(self, request_body):
        # TODO data_extractor dependent on data_type
        chat_id = request_body['message']['chat']['id']
        file_name = request_body['message']['document']['file_name']
        file_id = request_body['message']['document']['file_id']
        # TODO downloading via fileManager
        file_path = f'downloads/{file_name}'
        bot.download_file(file_id, file_path)
        bot.sendDocument(chat_id, open(file_path, 'rb'))
        os.remove(file_path)
