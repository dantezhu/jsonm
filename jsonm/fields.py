# -*- coding: utf-8 -*-

import copy


class BaseField(object):
    default = None
    null = None

    def __init__(self, default=None, null=False):
        self.default = copy.deepcopy(default)
        self.null = null

    def validate(self, value):
        if not self.null and value is None:
            raise ValueError('should not be None')

    def to_json(self, python_obj):
        return python_obj

    def to_python(self, json_obj):
        return json_obj


class Field(BaseField):
    """
    默认用这个就够了
    """
    pass


class DateTimeField(BaseField):
    """
    datetime
    """


class DateField(BaseField):
    """
    date
    """


class TimeField(BaseField):
    """
    time
    """
