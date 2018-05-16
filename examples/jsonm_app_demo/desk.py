# -*- coding: utf-8 -*-

from __future__ import print_function

from jsonm import Field, Model
from vals import jsonm_app


class Desk(Model):

    __jsonm_app__ = jsonm_app

    id = Field()
    current_uin = Field(default=-1)

    def __init__(self, id=None):
        super(Desk, self).__init__()
        # 默认
        self.id = id

    def on_from_json_over(self):
        print('%s.on_from_json_over' % self.__class__)

    def on_to_json_over(self, json_value):
        print('%s.on_to_json_over: %s' % (self.__class__, json_value))
