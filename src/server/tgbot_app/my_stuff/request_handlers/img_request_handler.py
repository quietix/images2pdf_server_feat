from src.server.setupConfig import bot
from .request_handler import RequestHandler
from src.server.tgbot_app.my_stuff.msgs.imgMsg import ImgMsg
import os


class ImgRequestHandler(RequestHandler):
    def handle_request(self, msg: ImgMsg):
        pass