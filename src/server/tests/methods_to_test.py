import unittest
from unittest.mock import patch, Mock
from src.server.tgbot_app.my_stuff.request_handlers.txt_handlers.common_cmds_handler import CommonCmdsHandler
from src.server.tgbot_app.my_stuff.request_handlers.txt_handlers.img_2_pdf_txt_handler import Img2PdfTxtHandler
from src.server.tgbot_app.my_stuff.request_handlers.txt_handlers.merge_pdf_txt_handler import MergePdfTxtHandler
from src.server.tgbot_app.my_stuff.factories.interaction_stuff_factories.img_2_pdf_factory import Img2PdfFactory
from src.server.tgbot_app.my_stuff.responses.img_2_pdf_creation_response import Img2PdfCreationResponse
from .variables import common_msgs, images2pdf_msgs, merge_pdf_msgs
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg


class TestStringMethods(unittest.TestCase):

    # @patch('src.server.tgbot_app.my_stuff.responses.common_response.CommonResponse.send_message')
    # def test_handle_request_common1(self, mock_send_message):
    #     # msg contains /help command
    #     msg = TxtMsg(common_msgs[0])
    #     handler = CommonCmdsHandler()
    #
    #     handler.handle_request(msg)
    #
    #     mock_send_message.assert_called_with(msg.chat_id,
    #                                          "Що можна зробити:\n\n1) /create_pdf - створити pdf із фото.\n\n2) /merge_pdf - об'єднати декілька pdf у один.\n\nОберіть необхідний варіант і дотримуйтесь вказівок.")
    #
    # @patch('src.server.tgbot_app.my_stuff.responses.common_response.CommonResponse.send_message')
    # def test_handle_request_common2(self, mock_send_message):
    #     # msg contains /start command
    #     msg = TxtMsg(common_msgs[1])
    #     handler = CommonCmdsHandler()
    #     handler.handle_request(msg)
    #     mock_send_message.assert_called_with(msg.chat_id,
    #                                          "Що можна зробити:\n\n1) /create_pdf - створити pdf із фото.\n\n2) /merge_pdf - об'єднати декілька pdf у один.\n\nОберіть необхідний варіант і дотримуйтесь вказівок.")
    #
    #
    # @patch('src.server.tgbot_app.my_stuff.responses.img_2_pdf_creation_response.Img2PdfCreationResponse.response_with_reply_keyboard_when_waiting_photos')
    # def test_handle_request_img2pdf_1(self, mock_response_with_reply_keyboard_when_waiting_photos):
    #     # msg contains /create_pdf command
    #     msg = TxtMsg(images2pdf_msgs[0])
    #     handler = Img2PdfTxtHandler()
    #     handler.handle_request(msg)
    #     mock_response_with_reply_keyboard_when_waiting_photos.assert_called()
    #
    # @patch('src.server.tgbot_app.my_stuff.responses.img_2_pdf_creation_response.Img2PdfCreationResponse.response_with_reply_keyboard_when_received_photos')
    # @patch('src.server.tgbot_app.my_stuff.responses.img_2_pdf_creation_response.Img2PdfCreationResponse.response_with_reply_keyboard_when_waiting_photos_state_2')
    # def test_handle_request_img2pdf_2(self, mock_response_with_reply_keyboard_when_waiting_photos_state_2, mock_response_with_reply_keyboard_when_received_photos):
    #     # msg contains <Створити pdf 🖼> command
    #     msg = TxtMsg(images2pdf_msgs[1])
    #     handler = Img2PdfTxtHandler()
    #     user_dir_composite = handler.get_file_manager().download_photos(msg.user_id)
    #     handler.handle_request(msg)
    #
    #     if len(user_dir_composite.children) == 0:
    #         mock_response_with_reply_keyboard_when_waiting_photos_state_2.assert_called()
    #     else:
    #         mock_response_with_reply_keyboard_when_received_photos.assert_called()
    #
    #
    # @patch('src.server.tgbot_app.my_stuff.responses.img_2_pdf_creation_response.Img2PdfCreationResponse.response_with_reply_keyboard_when_pdf_is_sent_creation')
    # def test_handle_request_img2pdf_3(self, mock_response_with_reply_keyboard_when_pdf_is_sent_creation):
    #     # msg contains <Автоматична назва 🖼> command
    #     msg = TxtMsg(images2pdf_msgs[2])
    #     handler = Img2PdfTxtHandler()
    #     handler.handle_request(msg)
    #     mock_response_with_reply_keyboard_when_pdf_is_sent_creation.assert_called()

    # @patch('src.server.tgbot_app.my_stuff.responses.merge_pdf_response.MergePdfResponse.response_with_reply_keyboard_when_opening_merge_session')
    # def test_handle_request_merge_pdf_1(self, mock_response_with_reply_keyboard_when_opening_merge_session):
    #     # msg contains /merge_pdf command
    #     msg = TxtMsg(merge_pdf_msgs[0])
    #     handler = MergePdfTxtHandler()
    #     handler.handle_request(msg)
    #     mock_response_with_reply_keyboard_when_opening_merge_session.assert_called()

    # @patch('src.server.tgbot_app.my_stuff.responses.merge_pdf_response.MergePdfResponse.response_with_reply_keyboard_when_received_pdfs')
    # @patch('src.server.tgbot_app.my_stuff.responses.merge_pdf_response.MergePdfResponse.response_with_reply_keyboard_when_waiting_pdfs_state_2')
    # def test_handle_request_merge_pdf_2(self, mock_response_with_reply_keyboard_when_waiting_pdfs_state_2, mock_response_with_reply_keyboard_when_received_pdfs):
    #     # msg contains <Об'єднати pdf 📂> command
    #     msg = TxtMsg(merge_pdf_msgs[1])
    #     handler = MergePdfTxtHandler()
    #     user_dir_composite = handler.get_file_manager().download_pdfs(msg.user_id)
    #     handler.handle_request(msg)
    #     if len(user_dir_composite.children) == 0:
    #         mock_response_with_reply_keyboard_when_waiting_pdfs_state_2.assert_called()
    #     else:
    #         mock_response_with_reply_keyboard_when_received_pdfs.assert_called()

    # @patch('src.server.tgbot_app.my_stuff.responses.merge_pdf_response.MergePdfResponse.response_with_reply_keyboard_when_pdf_is_sent_merge')
    # def test_handle_request_img2pdf_3(self, mock_response_with_reply_keyboard_when_pdf_is_sent_merge):
    #     # msg contains <Автоматична назва 📂> command
    #     msg = TxtMsg(merge_pdf_msgs[2])
    #     handler = MergePdfTxtHandler()
    #     handler.handle_request(msg)
    #     mock_response_with_reply_keyboard_when_pdf_is_sent_merge.assert_called()


if __name__ == '__main__':
    unittest.main()