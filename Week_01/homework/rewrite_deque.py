#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rewrite_deque.py    
@Contact :   13801489449@163.com
@License :   (C)Copyright 2019-2020,林间有风

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/26 1:00 下午   Jokky      1.0         None
'''
"""
Use add_first and add_last rewrite deque.
"""

class Deque(object):

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __call__(self):
        return self._data

    def is_empty(self):
        return len(self._data) == 0

    def add_first(self,value):
        return self._data.insert(0,value)

    def add_last(self,value):
        return self._data.append(value)

    def remove_first(self):
        if self.is_empty():
            raise Exception('deque is empty')
        self._data.pop(0)
        return True

    def remove_last(self):
        if self.is_empty():
            raise Exception('deque is empty')
        self._data.pop()
        return True

if __name__ == "__main__":
    deque = Deque()
    deque.add_first(1)
    deque.add_first(2)
    deque.add_last(3)
    print(deque())
    print(len(deque))