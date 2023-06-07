from .base_file import BaseFile
import os


class File(BaseFile):

    def delete_self(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def print_path(self):
        print(self.path)