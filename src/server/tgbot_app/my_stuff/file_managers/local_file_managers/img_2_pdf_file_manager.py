from src.server.tgbot_app.my_stuff.file_managers.local_file_manager import LocalFileManager
from src.server.tgbot_app.my_stuff.factories.msg_creator import Msg_Creator
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
from src.server.tgbot_app.my_stuff.msgs.imgMsg import ImgMsg
from src.server.tgbot_app.my_stuff.variables import downloads_path
from src.server.tgbot_app.my_stuff.variables import img_2_pdf_stop_commands
from src.server.tgbot_app.my_stuff.files_composite.file import File
from src.server.tgbot_app.my_stuff.files_composite.composite_file import CompositeFile
import os
import dotenv
import json
from PIL import Image, ImageOps


class Img2PdfFileManager(LocalFileManager):

    def download_photos(self, user_id) -> CompositeFile:
        if not os.path.exists(downloads_path):
            os.mkdir(downloads_path)

        if not os.path.exists(f'{downloads_path}/{user_id}'):
            os.mkdir(f'{downloads_path}/{user_id}')

        user_dir = CompositeFile(f'{downloads_path}/{user_id}')

        with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'r') as rd:
            data_list = json.load(rd)

        data_list.reverse()
        counter = 1

        for i in range(0, len(data_list)):
            msg = Msg_Creator.create_msg(data_list[i])
            if msg.user_id == user_id:
                if isinstance(msg, TxtMsg):
                    msg_text = msg.text
                    if msg_text in img_2_pdf_stop_commands:
                        break

                elif isinstance(msg, ImgMsg):
                    file_id = msg.file_id
                    file_name = f'image{counter}.jpg'
                    file_path = f'{downloads_path}/{user_id}/{file_name}'
                    user_dir.add_item(File(file_name))
                    counter += 1
                    self.response.download_file(file_id, file_path)

        return user_dir

    def create_photo_paths_list(self, user_id) -> CompositeFile:
        """Creates paths list from photos that exist in <user_id/> folder. Is used to prevent empty pdf creation try."""

        user_dir = CompositeFile(f'{downloads_path}/{user_id}')
        i = 1
        while 1:
            tmp_path = f'{downloads_path}/{user_id}/image{i}.jpg'
            if os.path.exists(tmp_path):
                user_dir.add_item(File(f'image{i}.jpg'))
                i += 1
            else:
                break
        return user_dir

    # when photo_list is ready
    def create_pdf_from_photo_list(self, user_dir_composite: CompositeFile, file_name) -> str:
        """
        Creates pdf file from photo paths in <user_id/> folder
        :param user_id: stands for the folder name where photos are stored
        :param photos_list: paths list of photos
        :param file_name: how you want name the file
        :return: path to created pdf
        """

        photos_count = len(user_dir_composite.children)
        image_list = []

        for i in range(photos_count - 1, -1, -1):
            tmp_path = user_dir_composite.children[i].path
            image = Image.open(tmp_path)
            image = ImageOps.exif_transpose(image)
            image_list.append(image)

        user_dir_composite.add_item(File(f'{file_name}.pdf'))

        image_list[0].save(user_dir_composite.children[-1].path, resolution=100.0, save_all=True,
                           append_images=image_list[1:])

        return user_dir_composite.children[-1].path