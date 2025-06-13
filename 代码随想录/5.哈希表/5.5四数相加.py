"""
Author: dpsfigo
Date: 2025-06-12 16:04:56
LastEditors: dpsfigo
LastEditTime: 2025-06-12 16:09:54
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/4sum-ii/
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1 之间，最终结果不会超过 2^31 - 1 。

例如:

输入:

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
输出:

2

解释:

两个元组如下:

(0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
(1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""


class Solution(object):
    def four_sum_ii(self, nums1, nums2, nums3, nums4) -> int:
        hashmap = dict()
        for i in nums1:
            for j in nums2:
                if i + j in hashmap:
                    hashmap[i + j] += 1
                else:
                    hashmap[i + j] = 1

        count = 0
        for i in nums3:
            for j in nums4:
                key = -(i + j)
                if key in hashmap:
                    count += hashmap[key]

        return count
