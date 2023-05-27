from src.server.tgbot_app.my_stuff.request_handlers import RequestHandler, TxtRequestHandler
from .handlers_controller import Handlers_Controller
from src.server.tgbot_app.my_stuff.msg import Msg, TxtMsg

class Main_Controller:
    @staticmethod
    def handle_request(request_body):
        handlers_controller = Handlers_Controller(request_body)
        handlers_controller.handle_request()