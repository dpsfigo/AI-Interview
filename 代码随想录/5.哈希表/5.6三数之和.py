"""
Author: dpsfigo
Date: 2025-06-13 14:05:14
LastEditors: dpsfigo
LastEditTime: 2025-06-20 16:56:44
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/3sum/

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意： 答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]
"""


class Solution(Object):
    def three_sum(self, nums: list) -> list:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                return result

            # 跳过相同的元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]

                if sum_ < 0:
                    left += 1
                elif sum_ > =:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # 跳过相同的元素以避免重复
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    while right > left and nums[left] == nums[left +1]:
                        left += 1

                    right -= 1
                    left += 1
        return result
