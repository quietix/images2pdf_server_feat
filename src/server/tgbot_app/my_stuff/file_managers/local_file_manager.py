import json
import os
import dotenv
from .base_file_manager import BaseFileManager
from ..factories.msg_creator import Msg_Creator
from src.server.tgbot_app.my_stuff.variables import ready_commands
from ..msgs.txtMsg import TxtMsg
import shutil
from src.server.tgbot_app.my_stuff.responses.img_2_pdf_creation_response import Img2PdfCreationResponse


class LocalFileManager(BaseFileManager):

    response = Img2PdfCreationResponse()

    @staticmethod
    def record_request(request_body):
        if os.path.exists(dotenv.dotenv_values('.env')['JSON_DATA_PATH']):
            with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'r') as f:
                data_list: list = json.load(f)

            data_list.append(request_body)

            with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'w') as f:
                json.dump(data_list, f, indent=4)

            try:
                LocalFileManager._clean_data_file()
            except:
                LocalFileManager._full_data_clean()
        else:
            data_list: list = [request_body]

            with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'w') as f:
                json.dump(data_list, f, indent=4)

            try:
                LocalFileManager._clean_data_file()
            except:
                LocalFileManager._full_data_clean()

    @staticmethod
    def _full_data_clean():
        with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'r') as rd:
            data_list: list = json.load(rd)
            data_list = [data_list[len(data_list) - 1]]

        with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'w') as fp:
            json.dump(data_list, fp, indent=4)

    @staticmethod
    def _clean_data_file():
        limit = int(dotenv.dotenv_values('.env')['DATA_LIST_LIMIT'])
        with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'r') as rd:
            data_list: list = json.load(rd)
            clear_num = int(len(data_list) / 2)
            if len(data_list) > limit:
                del data_list[:clear_num]

        with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'w') as fp:
            json.dump(data_list, fp, indent=4)

    @staticmethod
    def delete_directory(user_id):
        downloads_path = dotenv.dotenv_values('.env')['DOWNLOADS_PATH']
        if os.path.exists(f'{downloads_path}/{user_id}'):
            shutil.rmtree(f'{downloads_path}/{user_id}/')

    @staticmethod
    def get_last_non_command_message_text(user_id):
        with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'r') as f:
            data_list: list = json.load(f)
            data_list.reverse()
            for i in range(0, len(data_list)):
                msg = Msg_Creator.create_msg(data_list[i])
                tmp_user_id = msg.user_id
                if tmp_user_id == user_id:
                    if isinstance(msg, TxtMsg):
                        if msg.text in ready_commands:
                            next_msg = Msg_Creator.create_msg(data_list[i + 1])
                            if isinstance(next_msg, TxtMsg):
                                return next_msg.text

        return dotenv.dotenv_values('.env')['LAST_NON_COMMAND_NOT_FOUND_ERROR_CODE']