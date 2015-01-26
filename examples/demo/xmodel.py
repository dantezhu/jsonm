# -*- coding: utf-8 -*-

from jsonm import Model, json_loads, json_dumps


class XModel(Model):

    # 存储的前缀
    __prefix__ = None

    @classmethod
    def load(cls, rds, id):
        """
        从存储里读入
        """

        key = '%s:%s' % (cls.__prefix__ or cls.__name__, id)

        return json_loads(rds.get(key))

    def save(self, rds):

        key = '%s:%s' % (self.__class__.__prefix__ or self.__class__.__name__, self.id)

        return rds.set(key, json_dumps(self))

