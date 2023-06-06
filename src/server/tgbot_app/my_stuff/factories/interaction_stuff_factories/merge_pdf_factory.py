from src.server.tgbot_app.my_stuff.factories.interaction_stuff_factories.base_interaction_stuff_factory import BaseInteractionStuffFactory
from src.server.tgbot_app.my_stuff.file_managers.local_file_managers.merge_pdf_file_manager import MergePdfFileManager
from src.server.tgbot_app.my_stuff.responses.merge_pdf_response import MergePdfResponse


class MergePdfFactory(BaseInteractionStuffFactory):
    def get_file_manager(self) -> MergePdfFileManager:
        return MergePdfFileManager()

    def get_response(self) -> MergePdfResponse:
        return MergePdfResponse()