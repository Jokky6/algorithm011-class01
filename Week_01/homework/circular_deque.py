#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   circular_deque.py    
@Contact :   13801489449@163.com
@License :   (C)Copyright 2019-2020,林间有风

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/26 5:15 下午   Jokky      1.0         None
'''

class CircularDeque(object):

    def __init__(self,k):
        """
        Initialize your data structure here.
        Set the size of the deque to be k.
        :param k: deque size
        """
        self._size = 0
        self._front = 0
        self._rear = 0
        self._capacity = k
        self._data = [None] * k

    def __call__(self, *args, **kwargs):
        return self._data

    def __len__(self):
        return self._size

    def add_first(self,value):
        if self.is_full():
            raise Exception('circular deque is full')
        if self.is_empty():
            self._data[self._front] = value
        else:
            self._front = (self._front - 1) % self._capacity
            self._data[self._front] = value
        self._size += 1
        return True

    def add_last(self,value):
        if self.is_full():
            raise Exception('circular deque is full')
        if self.is_empty():
            self._data[self._rear] = value
        else:
            self._rear = (self._rear + 1) % self._capacity
            self._data[self._rear] = value
        self._size += 1
        return True

    def delete_first(self):
        if self.is_empty():
            raise Exception('circular deque is empty')
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        if self.is_empty():
            self._rear = self._front
        return True

    def delete_last(self):
        if self.is_empty():
            raise Exception('circular deque is empty')
        self._data[self._rear] = None
        self._rear = (self._rear - 1)% self._capacity
        self._size -= 1
        if self.is_empty():
            self._front = self._rear
        return True

    def get_first(self):
        return self._data[self._front]

    def get_last(self):
        return self._data[self._rear]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

if __name__ == "__main__":
    circular_deque = CircularDeque(10)
    print(circular_deque())
    circular_deque.add_first(1)
    circular_deque.add_last(2)
    circular_deque.add_last(3)
    circular_deque.add_first(7)
    print(circular_deque())
    circular_deque.delete_first()
    first = circular_deque.get_first()
    print(first)
    print(circular_deque())