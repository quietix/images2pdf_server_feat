import json
import os

import dotenv

from src.server.setupConfig import bot
from .file_manager import FileManager
from ..factories.msg_creator import Msg_Creator
from ..msgs.imgMsg import ImgMsg
from ..msgs.txtMsg import TxtMsg
import shutil
from PIL import Image, ImageOps

downloads_path = dotenv.dotenv_values('.env')['DOWNLOADS_PATH']


class LocalFileManager(FileManager):
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
    def download_photo(user_id) -> list[str]:
        if not os.path.exists(downloads_path):
            os.mkdir(dotenv.dotenv_values('.env')['DOWNLOADS_PATH'])
        with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'r') as rd:
            data_list = json.load(rd)
            data_list.reverse()
            photos_list = []
            counter = 1
            for i in range(0, len(data_list)):
                msg = Msg_Creator.create_msg(data_list[i])
                if msg.user_id == user_id:
                    if isinstance(msg, TxtMsg):
                        msg_text = msg.text
                        if msg_text == '/create_pdf' or msg_text == 'Завершити сеанс' or msg_text == 'Відмінити створення':
                            break

                    elif isinstance(msg, ImgMsg):
                        if not os.path.exists(f'{downloads_path}/{user_id}'):
                            os.mkdir(f'{downloads_path}/{user_id}')
                        file_id = msg.file_id
                        file_name = f'image{counter}.jpg'
                        file_path = f'{downloads_path}/{user_id}/{file_name}'
                        counter += 1
                        photos_list.append(file_path)
                        bot.download_file(file_id, file_path)

        return photos_list

    @staticmethod
    def delete_directory(user_id):
        if os.path.exists(f'{downloads_path}/{user_id}'):
            shutil.rmtree(f'{downloads_path}/{user_id}/')

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
    def create_photo_list_from_existing_files_in_directory(user_id):
        photo_list = []
        i = 1
        while 1:
            if os.path.exists(f'{downloads_path}/{user_id}/image{i}.jpg'):
                photo_list.append(f'{downloads_path}/{user_id}/image{i}.jpg')
                i += 1
            else:
                break
        return photo_list

    @staticmethod
    # when photo_list is ready
    def create_pdf_from_photo_list(user_id, photos_list: list, file_name):
        photos_count = len(photos_list)
        image_list = []

        for i in range(photos_count - 1, -1, -1):
            image = Image.open(f'{downloads_path}/{user_id}/image{i + 1}.jpg')
            image = ImageOps.exif_transpose(image)
            image_list.append(image)

        image_list[0].save(f'{downloads_path}/{user_id}/{file_name}.pdf', resolution=100.0, save_all=True,
                           append_images=image_list[1:])

        return f'{downloads_path}/{user_id}/{file_name}.pdf'

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
                        if msg.text == "/ready":
                            next_msg = Msg_Creator.create_msg(data_list[i+1])
                            if isinstance(next_msg, TxtMsg):
                                return next_msg.text

        return dotenv.dotenv_values('.env')['LAST_NON_COMMAND_NOT_FOUND_ERROR_CODE']