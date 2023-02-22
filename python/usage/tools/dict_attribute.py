#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @File    :   dict_attribute.py
# @Time    :   2022/11/30 13:47 
# @Author  :   zhenyu.hu
# @Desc    :   <awaiting description>

import typing as t


class ConfigAttribute:
    """Makes an attribute forward to the config"""

    def __init__(self, name: str, get_converter: t.Optional[t.Callable] = None) -> None:
        self.__name__ = name
        self.get_converter = get_converter

    def __get__(self, obj: t.Any, owner: t.Any = None) -> t.Any:
        if obj is None:
            return self
        rv = obj.config[self.__name__]
        if self.get_converter is not None:
            rv = self.get_converter(rv)
        return rv

    def __set__(self, obj: t.Any, value: t.Any) -> None:
        obj.config[self.__name__] = value


class DictAttribute:
    """Dict interface to attributes.

    `obj[k] -> obj.k`
    `obj[k] = val -> obj.k = val`
    """

    obj = None

    def __init__(self, obj):
        # type: (t.Any) -> None
        object.__setattr__(self, 'obj', obj)

    def __getattr__(self, key):
        # type: (t.Any) -> t.Any
        return getattr(self.obj, key)

    def __setattr__(self, key, value):
        # type: (t.Any, t.Any) -> None
        return setattr(self.obj, key, value)

    def get(self, key, default=None):
        # type: (t.Any, t.Any) -> t.Any
        try:
            return self[key]
        except KeyError:
            return default

    def setdefault(self, key, default=None):
        # type: (t.Any, t.Any) -> None
        if key not in self:
            self[key] = default

    def __getitem__(self, key):
        # type: (t.Any) -> t.Any
        try:
            return getattr(self.obj, key)
        except AttributeError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        # type: (t.Any, t.Any) -> t.Any
        setattr(self.obj, key, value)

    def __contains__(self, key):
        # type: (t.Any) -> bool
        return hasattr(self.obj, key)

    def _iterate_keys(self):
        # type: () -> t.Iterable
        return iter(dir(self.obj))

    iterkeys = _iterate_keys

    def __iter__(self):
        # type: () -> t.Iterable
        return self._iterate_keys()

    def _iterate_items(self):
        # type: () -> t.Iterable
        for key in self._iterate_keys():
            yield key, getattr(self.obj, key)

    iteritems = _iterate_items

    def _iterate_values(self):
        # type: () -> t.Iterable
        for key in self._iterate_keys():
            yield getattr(self.obj, key)

    itervalues = _iterate_values

    items = _iterate_items
    keys = _iterate_keys
    values = _iterate_values
