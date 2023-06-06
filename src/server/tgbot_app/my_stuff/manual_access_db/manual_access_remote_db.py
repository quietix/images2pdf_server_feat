from .manual_access_db import ManualAccessDB
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg


class ManualAccessRemoteDB(ManualAccessDB):
    def total_cleanup(self, msg: TxtMsg):
        print("Conducting cleanup...")