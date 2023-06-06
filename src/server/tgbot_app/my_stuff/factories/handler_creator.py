from src.server.tgbot_app.my_stuff.request_handlers.request_handler import RequestHandler
from src.server.tgbot_app.my_stuff.request_handlers.img_request_handler import ImgRequestHandler
from src.server.tgbot_app.my_stuff.request_handlers.txt_handlers.common_cmds_handler import CommonCmdsHandler
from src.server.tgbot_app.my_stuff.request_handlers.txt_handlers.img_2_pdf_txt_handler import Img2PdfTxtHandler
from src.server.tgbot_app.my_stuff.request_handlers.txt_handlers.merge_pdf_txt_handler import MergePdfTxtHandler
from src.server.tgbot_app.my_stuff.request_handlers.file_request_handler import FileRequestHandler
from src.server.tgbot_app.my_stuff.request_handlers.not_created_request_handler import NotCreatedRequestHandler

from src.server.tgbot_app.my_stuff.msgs.msg import Msg
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
from src.server.tgbot_app.my_stuff.msgs.imgMsg import ImgMsg
from src.server.tgbot_app.my_stuff.msgs.fileMsg import FileMsg


class Handler_Creator:

    # Factory method
    @staticmethod
    def create_handler(msg: Msg) -> RequestHandler:

        if isinstance(msg, TxtMsg):
            common_cms_handler = CommonCmdsHandler()
            img_handler = Img2PdfTxtHandler()
            merge_handler = MergePdfTxtHandler()

            common_cms_handler.set_next(img_handler).set_next(merge_handler)

            return common_cms_handler

        elif isinstance(msg, ImgMsg):
            return ImgRequestHandler()

        elif isinstance(msg, FileMsg):
            return FileRequestHandler()

        return NotCreatedRequestHandler()