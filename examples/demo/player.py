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

    def on_from_json_over(self):
        print '%s.on_from_json_over' % self.__class__

    def on_to_json_over(self):
        print '%s.on_to_json_over' % self.__class__
