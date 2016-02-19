# -*- coding: utf-8 -*-

import json


class Application(object):
    """
    应用
    """

    # 被定义过的models
    _defined_models = None

    def __init__(self):
        """
        初始化
        :return:
        """
        self._defined_models = dict()

    def _custom_dumps(self, python_object):
        if python_object.__class__.__name__ in self._defined_models:
            model = self._defined_models[python_object.__class__.__name__]

            if isinstance(model, dict):
                return model['to_json'](python_object)
            else:
                return python_object.to_json()

        # print python_object
        raise TypeError(repr(python_object) + ' is not JSON serializable')

    def _custom_loads(self, json_object):
        if '__class__' in json_object:
            model = self._defined_models.get(json_object['__class__'])
            if model is not None:
                if isinstance(model, dict):
                    return model['from_json'](json_object)
                else:
                    obj = model()
                    obj.from_json(json_object)
                    return obj

        return json_object

    def json_dumps(self, *args, **kwargs):
        kwargs.update(dict(
            default=self._custom_dumps
        ))

        return json.dumps(*args, **kwargs)

    def json_loads(self, *args, **kwargs):
        kwargs.update(dict(
            object_hook=self._custom_loads
        ))

        return json.loads(*args, **kwargs)

    def register_models(self, models):
        """
        注册models
        :param models:
            model可以为两种类型:
                1. 自定义类，比如Desk，这种可以自己内部实现to_json 和 from_json 的。
                2. 系统内置类，比如datetime，这种我们没法修改其内部。
                    {
                        'type': datetime,
                        'to_json': xxx,
                        'from_json': yyy,
                    }
            :return:
        """
        self._defined_models.update(
            dict([(model['type'].__name__ if isinstance(model, dict) else model.__name__, model) for model in models])
        )

    def register_default_models(self):
        """
        注册默认支持的序列化类型，主要是日期和时间
        :return:
        """
        import datetime

        def datetime_to_json(python_object):
            fmt = '%Y-%m-%d %H:%M:%S.%f'
            return dict(
                __class__=python_object.__class__.__name__,
                __value__=python_object.strftime(fmt),
            )

        def datetime_from_json(json_object):
            json_value = json_object['__value__']
            fmt = '%Y-%m-%d %H:%M:%S.%f'
            return datetime.datetime.strptime(json_value, fmt)

        def date_to_json(python_object):
            fmt = '%Y-%m-%d'
            return dict(
                __class__=python_object.__class__.__name__,
                __value__=python_object.strftime(fmt),
            )

        def date_from_json(json_object):
            json_value = json_object['__value__']
            fmt = '%Y-%m-%d'
            return datetime.datetime.strptime(json_value, fmt).date()

        self.register_models((
            dict(
                type=datetime.datetime,
                to_json=datetime_to_json,
                from_json=datetime_from_json,
            ), dict(
                type=datetime.date,
                to_json=date_to_json,
                from_json=date_from_json,
            )
        ))
