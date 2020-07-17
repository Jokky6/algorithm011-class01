#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   index.py    
@Contact :   13801489449@163.com
@License :   (C)Copyright 2019-2020,林间有风

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/17 10:43 上午   Jokky      1.0         None
'''

# 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
from typing import List


class Solution(object):
    def binary_search(self,nums:List[int]):
        left , right = 0 , len(nums)-1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

if __name__ == '__main__':
    search = Solution()
    result = search.binary_search([4, 5, 6, 7, 1, 2])
    print(result)