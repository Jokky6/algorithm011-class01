# 给你两个数组，arr1 和 arr2，

# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr_set = set(arr2)
        order_dic = {key:value for key,value in zip(arr2, [i for i in range(len(arr2))])}
        in_list = []
        not_in_list = []
        for i in arr1:
            if i not in arr_set:
                not_in_list.append(i)
            else:
                in_list.append(i)
        for index, num in enumerate(in_list):
            in_list[index] = (num, order_dic[num])
        in_list.sort(key=lambda item: item[1])
        return [i[0] for i in in_list] + sorted(not_in_list)