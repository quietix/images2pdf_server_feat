from .request_handlers import TxtRequestHandler, ImgRequestHandler, FileRequestHandler

# def handle(request_body):
#     chat_id = request_body['message']['chat']['id']
#     bot.sendMessage(chat_id, 'hello')

class Controller:
    @staticmethod
    def handle_request(request_body):
        requestHandler = TxtRequestHandler()
        requestHandler.handle_request(request_body)

    # TODO
    @staticmethod
    def detect_msg_type():
        pass