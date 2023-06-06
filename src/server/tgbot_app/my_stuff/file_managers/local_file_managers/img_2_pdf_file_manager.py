from src.server.tgbot_app.my_stuff.file_managers.local_file_manager import LocalFileManager
from src.server.tgbot_app.my_stuff.factories.msg_creator import Msg_Creator
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
from src.server.tgbot_app.my_stuff.msgs.imgMsg import ImgMsg
from src.server.tgbot_app.my_stuff.variables import downloads_path
from src.server.tgbot_app.my_stuff.variables import img_2_pdf_stop_commands
import os
import dotenv
import json
from PIL import Image, ImageOps


class Img2PdfFileManager(LocalFileManager):

    def download_photos(self, user_id) -> list[str]:
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
                        if msg_text in img_2_pdf_stop_commands:
                            break

                    elif isinstance(msg, ImgMsg):
                        if not os.path.exists(f'{downloads_path}/{user_id}'):
                            os.mkdir(f'{downloads_path}/{user_id}')
                        file_id = msg.file_id
                        file_name = f'image{counter}.jpg'
                        file_path = f'{downloads_path}/{user_id}/{file_name}'
                        counter += 1
                        photos_list.append(file_path)
                        self.response.download_file(file_id, file_path)

        return photos_list

    def create_photo_paths_list(self, user_id) -> list[str]:
        """Creates paths list from photos that exist in <user_id/> folder. Is used to prevent empty pdf creation try."""

        photo_list = []
        i = 1
        while 1:
            if os.path.exists(f'{downloads_path}/{user_id}/image{i}.jpg'):
                photo_list.append(f'{downloads_path}/{user_id}/image{i}.jpg')
                i += 1
            else:
                break
        return photo_list

    # when photo_list is ready
    def create_pdf_from_photo_list(self, user_id, photos_list: list, file_name) -> str:
        """
        Creates pdf file from photo paths in <user_id/> folder
        :param user_id: stands for the folder name where photos are stored
        :param photos_list: paths list of photos
        :param file_name: how you want name the file
        :return: path to created pdf
        """

        photos_count = len(photos_list)
        image_list = []

        for i in range(photos_count - 1, -1, -1):
            image = Image.open(f'{downloads_path}/{user_id}/image{i + 1}.jpg')
            image = ImageOps.exif_transpose(image)
            image_list.append(image)

        image_list[0].save(f'{downloads_path}/{user_id}/{file_name}.pdf', resolution=100.0, save_all=True,
                           append_images=image_list[1:])

        return f'{downloads_path}/{user_id}/{file_name}.pdf'