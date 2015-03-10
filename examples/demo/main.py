# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../../')
from jsonm import register_models
from desk import Desk
from player import Player
from redis import StrictRedis

rds = StrictRedis()


def main():
    register_models((Desk, Player))

    desk = Desk(2)
    desk.current_uin = 1
    desk.players[0] = Player(0, 'dante0')
    desk.players[1] = Player(1, 'dante1')
    desk.players[2] = Player(2, 'dante2')
    desk.players[3] = Player(3, 'dante3')
    desk.players[4] = Player(4, 'dante4')

    print 'desk:', desk

    desk.save(rds)

    desk = Desk.load(rds, 2)

    print 'desk:', desk

if __name__ == '__main__':
    main()
