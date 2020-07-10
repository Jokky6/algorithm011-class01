#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   permutations.py    
@Contact :   13801489449@163.com
@License :   (C)Copyright 2019-2020,林间有风

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/10 2:17 下午   Jokky      1.0         None
'''

# 全队列

# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
import itertools
from typing import List


class Solution(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:return [nums]
        res = []
        for i, num in enumerate(nums):
            rest = nums[:i] + nums[i + 1:]
            for rest_num in self.permute(rest):
                res.append([num] + rest_num)
        return res

# class Solution(object):
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return list(itertools.permutations(nums))