from src.server.tgbot_app.my_stuff.factories.interaction_stuff_factories.base_interaction_stuff_factory import BaseInteractionStuffFactory
from src.server.tgbot_app.my_stuff.file_managers.local_file_managers.img_2_pdf_file_manager import Img2PdfFileManager
from src.server.tgbot_app.my_stuff.responses.img_2_pdf_creation_response import Img2PdfCreationResponse


class Img2PdfFactory(BaseInteractionStuffFactory):
    def get_file_manager(self) -> Img2PdfFileManager:
        return Img2PdfFileManager()

    def get_response(self) -> Img2PdfCreationResponse:
        return Img2PdfCreationResponse()