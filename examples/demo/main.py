# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
sys.path.insert(0, '../../')
import datetime
from jsonm import register_models
from desk import Desk
from player import Player
from redis import StrictRedis
from jsonm.contrib import DATETIME_MODELS

rds = StrictRedis()


def main():
    register_models(DATETIME_MODELS)
    register_models((Desk, Player))

    desk = Desk(7)
    desk.current_uin = 1
    desk.players[0] = Player(0, 'dante0')
    desk.players[1] = Player(1, 'dante1')
    desk.players[2] = Player(2, 'dante2')
    desk.players[3] = Player(3, 'dante3')
    desk.players[4] = Player(4, 'dante4')

    print('desk:', desk)

    desk.save(rds)

    desk = Desk.load(rds, 7)

    print('desk:', desk)

if __name__ == '__main__':
    main()
