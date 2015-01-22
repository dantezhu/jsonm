# -*- coding: utf-8 -*-

from jsonm import Field, Model


class Desk(Model):

    __prefix__ = 'desk'

    id = Field()
    current_uin = Field(default=-1)
    players = Field(default=[None for it in xrange(0, 5)])

    def __init__(self, id=None):
        super(Desk, self).__init__()
        # 默认
        self.id = id

    @property
    def current_player(self):
        """
        主要解决引用player对象的问题
        :return:
        """
        for player in self.players:
            if player and self.current_uin == player.id:
                return player
        return None

    @current_player.setter
    def current_player(self, value):
        self.current_uin = value.id if value else -1
