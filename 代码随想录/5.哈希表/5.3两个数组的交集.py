"""
Author: dpsfigo
Date: 2025-06-11 17:07:04
LastEditors: dpsfigo
LastEditTime: 2025-06-11 17:07:50
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/intersection-of-two-arrays/

给定两个数组 nums1 和 nums2 ，返回 它们的 交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的


提示：

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""


class Solution:
    def intersection_of_two_arrays_v1(self, nums1: list, nums2: list) -> list:
        return list(set(nums1) & set(nums2))

    def intersection_of_two_arrays_v2(self, nums1: list, nums2: list) -> list:
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1

        ret = []
        for num in nums2:
            if num in table.keys():
                ret.append(num)
                del table[num]
        return ret


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    sol = Solution()
    ret = sol.intersection_of_two_arrays_v2(nums1, nums2)
    print(ret)
