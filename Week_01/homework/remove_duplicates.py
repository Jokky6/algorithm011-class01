#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   remove_duplicates.py    
@Contact :   13801489449@163.com
@License :   (C)Copyright 2019-2020,林间有风

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/26 3:52 下午   Jokky      1.0         None
'''
from typing import List

"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""

# 从nums的最后一个开始遍历, 然后与前一个进行对比.
# 如果相等, 则删除该位置的数.
# 不等, 则继续往前遍历.


# 解法一：
class SolutionOne:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)

# 解法二：
class SolutionTwo:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
        return count+1