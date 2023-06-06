from ..manual_access_db import ManualAccessDB
from ..manual_access_local_db import ManualAccessLocalDB
from src.server.tgbot_app.my_stuff.msgs.txtMsg import TxtMsg
from src.server.tgbot_app.my_stuff.responses.base_response import BaseResponse
import dotenv


# Proxy
class ManualAccessLocalDBProxy(ManualAccessDB):

    _db_manager: ManualAccessLocalDB

    def __init__(self, db_manager: ManualAccessLocalDB):
        self._db_manager = db_manager

    def total_cleanup(self, msg: TxtMsg):
        if self._check_access(msg):
            BaseResponse.send_message(msg.chat_id, "Conducting cleanup...")
            self._db_manager.total_cleanup(msg)
            BaseResponse.send_message(msg.chat_id, "Cleanup is successfully done")
        else:
            BaseResponse.send_message(msg.chat_id, "You don't have admin privileges")

    def _check_access(self, msg: TxtMsg) -> bool:
        admin_id = dotenv.dotenv_values('.env')['ADMIN_ID']
        if str(msg.user_id) == str(admin_id):
            return True
        return False