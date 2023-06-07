from .handlers_controller import Handlers_Controller
from ..factories.msg_creator import Msg_Creator
from ..factories.handler_creator import Handler_Creator
from ..file_managers.local_file_manager import LocalFileManager

class Main_Controller:
    @staticmethod
    def handle_request(request_body):
        file_manager = LocalFileManager()
        file_manager.record_request(request_body)

        msg = Msg_Creator.create_msg(request_body)
        handler = Handler_Creator.create_handler(msg)

        handlers_controller = Handlers_Controller(msg, handler)
        handlers_controller.handle_request()