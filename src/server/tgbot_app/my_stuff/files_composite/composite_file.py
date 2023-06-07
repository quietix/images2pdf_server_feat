from .base_file import BaseFile
import os


class CompositeFile(BaseFile):

    children: list[BaseFile]

    def __init__(self, path):
        super().__init__(path)
        self.children = []

    def delete_self(self):
        # deleting children
        for file in self.children:
            file.delete_self()

        # deleting self
        if os.path.exists(self.path) and len(os.listdir(self.path)) == 0:
            os.rmdir(self.path)

    def add_item(self, item: BaseFile):
        self.children.append(item)
        item.path = self.path + '/' + item.path

    def remove_item(self, item: BaseFile):
        self.children.remove(item)

    def print_path(self):
        for file in self.children:
            file.print_path()