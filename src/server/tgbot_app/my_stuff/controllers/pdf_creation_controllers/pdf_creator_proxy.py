from .pdf_creator import PdfCreator
from .standard_pdf_creator import StandardPdfCreator
from ...response import Response
from ...file_manager.local_file_manager import LocalFileManager


# Proxy
class PdfCreatorProxy(PdfCreator):

    _standardPdfCreator: StandardPdfCreator

    def __init__(self, chat_id, user_id):
        super().__init__(chat_id, user_id)
        self._standardPdfCreator = StandardPdfCreator(chat_id, user_id)

    def open_session(self):
        self._standardPdfCreator.open_session()

    def invoke_creation(self):
        photo_list = LocalFileManager.download_photo(self.user_id)
        if len(photo_list) <= 0:
            Response.response_with_reply_keyboard_when_waiting_photos_state_2(self.chat_id)
        else:
            self._standardPdfCreator.invoke_creation()

    def cancel_creation(self):
        self._standardPdfCreator.cancel_creation()

    def create_with_auto_name(self):
        self._standardPdfCreator.create_with_auto_name()

    def continue_creation(self):
        self._standardPdfCreator.continue_creation()

    def end_session(self):
        self._standardPdfCreator.end_session()

    def prepare_custom_name(self):
        self._standardPdfCreator.prepare_custom_name()

    def create_with_custom_name(self):
        self._standardPdfCreator.create_with_custom_name()