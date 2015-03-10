# -*- coding: utf-8 -*-

from .fields import BaseField


class Model(object):

    def __init__(self):
        for attr, field_def in self._fields_dict().items():
            setattr(self, attr, field_def.default)

    def to_json(self):
        """
        导出为json
        :return:
        """
        self.validate()

        value = dict()
        for attr, field_def in self._fields_dict().items():
            json_value = field_def.to_json(getattr(self, attr, None))
            value[attr] = json_value

        return dict(
            __class__=self.__class__.__name__,
            __value__=value
        )

    def from_json(self, json_str):
        """
        从json解析
        :param json_str:
        :return:
        """

        json_value = json_str['__value__']

        for attr, field_def in self._fields_dict().items():
            python_value = field_def.to_python(json_value.get(attr))
            setattr(self, attr, python_value)

    def _fields_dict(self):
        """
        获取fields
        :return:
        """

        fields_dict = dict()

        for attr in dir(self.__class__):
            val = getattr(self.__class__, attr)
            if isinstance(val, BaseField):
                fields_dict[attr] = val

        return fields_dict

    def validate(self):
        """
        验证参数是否合法
        :return:
        """

        for attr, field_def in self._fields_dict().items():
            try:
                field_def.validate(getattr(self, attr, None))
            except Exception, e:
                raise ValueError('%s.%s validate fail. %s' % (self.__class__.__name__, attr, e.message))

    def __str__(self):
        from .utils import json_dumps

        return json_dumps(self, indent=4)
