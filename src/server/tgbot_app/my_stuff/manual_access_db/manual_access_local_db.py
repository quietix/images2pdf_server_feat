from .manual_access_db import ManualAccessDB
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
import dotenv
import json


class ManualAccessLocalDB(ManualAccessDB):
    def total_cleanup(self, msg: TxtMsg):
        with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'r') as rd:
            data_list: list = json.load(rd)
            data_list = [data_list[len(data_list) - 1]]

        with open(dotenv.dotenv_values('.env')['JSON_DATA_PATH'], 'w') as fp:
            json.dump(data_list, fp, indent=4)