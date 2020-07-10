#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   permutations-ii.py    
@Contact :   13801489449@163.com
@License :   (C)Copyright 2019-2020,林间有风

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/10 4:11 下午   Jokky      1.0         None
'''
# 全队列

# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
from functools import reduce
from typing import List


class Solution(object):
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda perms, n: [p[:i] + [n] + p[i:]
                                        for p in perms
                                        for i in range((p + [n]).index(n) + 1)],
                      nums, [[]])