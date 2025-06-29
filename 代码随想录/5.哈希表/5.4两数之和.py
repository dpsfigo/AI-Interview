"""
Author: dpsfigo
Date: 2025-06-12 10:29:25
LastEditors: dpsfigo
LastEditTime: 2025-06-12 10:36:39
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/two-sum/
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]
"""


class Solution:
    def two_sum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            if target - nums[i] in nums:
                return [i, nums.index(target - nums[i])]
        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    ret = sol.two_sum(nums, target)
    print(ret)
