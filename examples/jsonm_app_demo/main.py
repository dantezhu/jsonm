# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
sys.path.insert(0, '../../')
import datetime
from desk import Desk
from vals import jsonm_app


def main():
    jsonm_app.register_models((Desk,))

    desk = Desk(7)
    desk.current_uin = 1

    str_json = jsonm_app.json_dumps(desk, indent=4)

    print(str_json)

    desk = jsonm_app.json_loads(str_json)

    print(desk)

if __name__ == '__main__':
    main()
