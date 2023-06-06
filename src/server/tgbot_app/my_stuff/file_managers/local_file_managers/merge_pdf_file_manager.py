from src.server.tgbot_app.my_stuff.file_managers.local_file_manager import LocalFileManager
from src.server.tgbot_app.my_stuff.factories.msg_creator import Msg_Creator
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
from src.server.tgbot_app.my_stuff.msgs.fileMsg import FileMsg
from src.server.tgbot_app.my_stuff.variables import downloads_path
from pypdf import PdfMerger
from src.server.tgbot_app.my_stuff.variables import merge_pdf_stop_commands
import os
import dotenv
import json


class MergePdfFileManager(LocalFileManager):

    def download_pdfs(self, user_id) -> list[str]:
        if not os.path.exists(downloads_path):
            os.mkdir(dotenv.dotenv_values('.env')['DOWNLOADS_PATH'])
        with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'r') as rd:
            data_list = json.load(rd)
            data_list.reverse()
            pdf_list = []
            counter = 1
            for i in range(0, len(data_list)):
                msg = Msg_Creator.create_msg(data_list[i])
                if msg.user_id == user_id:
                    if isinstance(msg, TxtMsg):
                        msg_text = msg.text
                        if msg_text in merge_pdf_stop_commands:
                            break

                    elif isinstance(msg, FileMsg):
                        if not os.path.exists(f'{downloads_path}/{user_id}'):
                            os.mkdir(f'{downloads_path}/{user_id}')

                        if os.path.splitext(msg.file_name)[1] == '.pdf':
                            file_id = msg.file_id
                            file_name = f'file{counter}.pdf'
                            file_path = f'{downloads_path}/{user_id}/{file_name}'
                            counter += 1
                            pdf_list.append(file_path)
                            self.response.download_file(file_id, file_path)

        return pdf_list

    def create_pdf_paths_list(self, user_id) -> list[str]:
        """Creates paths list from pdf files that exist in <user_id/> folder. Is used to prevent empty pdf creation try."""

        pdf_list = []
        i = 1
        while 1:
            if os.path.exists(f'{downloads_path}/{user_id}/file{i}.pdf'):
                pdf_list.append(f'{downloads_path}/{user_id}/file{i}.pdf')
                i += 1
            else:
                break

        return pdf_list

    # when pdf_list is ready
    def create_pdf_from_pdf_list(self, user_id, pdf_list: list, file_name) -> str:
        """
        Merges pdf files in <user_id/> folder
        :param user_id: stands for the folder name where photos are stored
        :param pdf_list: paths list of pdf files
        :param file_name: how you want name the file
        :return: path to new pdf
        """

        pdf_count = len(pdf_list)
        pdfMerger = PdfMerger()

        for i in range(pdf_count, 0, -1):
            pdfMerger.append(f'{downloads_path}/{user_id}/file{i}.pdf')

        final_path = f'{downloads_path}/{user_id}/{file_name}.pdf'
        pdfMerger.write(final_path)
        pdfMerger.close()

        return final_path