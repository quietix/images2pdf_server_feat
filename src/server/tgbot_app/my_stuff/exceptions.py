from abc import ABC


class MsgNotCreated(Exception):
    pass


class TxtMsgNotCreated(MsgNotCreated):
    def __init__(self):
        super().__init__('Could not find <text> filed in request body')