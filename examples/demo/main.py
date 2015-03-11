# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../../')
import datetime
from jsonm import register_models
from desk import Desk
from player import Player
from redis import StrictRedis

rds = StrictRedis()


def datetime_to_json(python_object):
    format = '%Y-%m-%d %H:%M:%S.%f'
    return dict(
        __class__=python_object.__class__.__name__,
        __value__=python_object.strftime(format),
    )


def datetime_from_json(json_object):
    json_value = json_object['__value__']
    format = '%Y-%m-%d %H:%M:%S.%f'
    return datetime.datetime.strptime(json_value, format)


def main():
    register_models((Desk, Player, dict(
        type=datetime.datetime,
        to_json=datetime_to_json,
        from_json=datetime_from_json,
    )))

    desk = Desk(7)
    desk.current_uin = 1
    desk.players[0] = Player(0, 'dante0')
    desk.players[1] = Player(1, 'dante1')
    desk.players[2] = Player(2, 'dante2')
    desk.players[3] = Player(3, 'dante3')
    desk.players[4] = Player(4, 'dante4')

    print 'desk:', desk

    desk.save(rds)

    desk = Desk.load(rds, 7)

    print 'desk:', desk

if __name__ == '__main__':
    main()
