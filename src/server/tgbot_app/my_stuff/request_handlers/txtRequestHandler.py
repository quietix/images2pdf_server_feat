from src.server.setupConfig import bot
from .requestHandler import RequestHandler
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg


class TxtRequestHandler(RequestHandler):
    def handle_request(self, msg: TxtMsg):
        bot.sendMessage(msg.chat_id, msg.text)