#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rotate_array.py    
@Contact :   13801489449@163.com
@License :   (C)Copyright 2019-2020,林间有风

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/26 4:33 下午   Jokky      1.0         None
'''
from typing import List

"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
         Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums[:] = nums[length-k:] + nums[:length-k]
