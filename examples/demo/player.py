# -*- coding: utf-8 -*-

from jsonm import Field
from xmodel import XModel


class Player(XModel):
    id = Field()
    nick = Field()

    def __init__(self, id=None, nick=None):
        super(Player, self).__init__()
        self.id = id
        self.nick = nick
