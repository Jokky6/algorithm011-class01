# 合并区间

# 给出一个区间的集合，请合并所有重叠的区间。
from typing import List


class Solution(object):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key=lambda x: (x[0], x[1]))
        answer = [intervals[0]]

        for i in range(1, len(intervals)):
            if answer[-1][0] == intervals[i][0]:
                answer[-1][1] = intervals[i][1]
            elif answer[-1][1] >= intervals[i][0]:
                answer[-1][1] = max(answer[-1][1], intervals[i][1])
            else:
                answer.append(intervals[i])

        return answer