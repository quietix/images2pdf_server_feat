class MsgNotCreated(Exception):
    pass


class TxtMsgNotCreated(MsgNotCreated):
    def __init__(self):
        super().__init__('Could not find <text> filed in request body')


class ImgMsgNotCreated(MsgNotCreated):
    def __init__(self):
        super().__init__('Could not find <photo> filed in request body')


class FileMsgNotCreated(MsgNotCreated):
    def __init__(self):
        super().__init__('Could not find <document> filed in request body')