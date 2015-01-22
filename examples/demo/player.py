# -*- coding: utf-8 -*-

from jsonm import Model, Field


class Player(Model):
    id = Field()
    nick = Field()

    def __init__(self, id=None, nick=None):
        super(Player, self).__init__()
        self.id = id
        self.nick = nick
