from src.server.setupConfig import bot
from .requestHandler import RequestHandler
from src.server.tgbot_app.my_stuff.msgs.fileMsg import FileMsg
import os


class FileRequestHandler(RequestHandler):
    def handle_request(self, msg: FileMsg):
        pass