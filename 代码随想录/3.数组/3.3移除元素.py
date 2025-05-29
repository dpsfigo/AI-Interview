"""
Author: dpsfigo
Date: 2025-05-29 17:50:50
LastEditors: dpsfigo
LastEditTime: 2025-05-29 17:51:31
Description: 请填写简介
"""

"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例 1: 给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。 你不需要考虑数组中超出新长度后面的元素。
示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
你不需要考虑数组中超出新长度后面的元素。
"""


class Solution:
    def remove_element(self, nums: list[int], val: int) -> int:
        fast = 0
        slow = 0
        while fast < len(nums) - 1:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    sol = Solution()
    result = sol.remove_element(nums, val)
    print(result)
