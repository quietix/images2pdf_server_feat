from src.server.setupConfig import bot
from .request_handler import RequestHandler
from src.server.tgbot_app.my_stuff.msgs.msg import Msg


class NotCreatedRequestHandler(RequestHandler):
    def handle_request(self, msg: Msg):
        bot.sendMessage(msg.chat_id, 'Wrong message type. Try again!')
