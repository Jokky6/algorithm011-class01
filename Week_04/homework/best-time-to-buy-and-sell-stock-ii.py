#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   best-time-to-buy-and-sell-stock-ii.py    
@Contact :   13801489449@163.com
@License :   (C)Copyright 2019-2020,林间有风

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/17 9:25 上午   Jokky      1.0         None
'''

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 贪心算法

from typing import List


# class Solution(object):
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for i in range(1,len(prices)):
#             tmp = prices[i] - prices[i-1]
#             if tmp >0:
#                 profit+=tmp
#         return profit

class Solution(object):
    def maxProfit(self, prices:List[int]) -> int:
        return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))