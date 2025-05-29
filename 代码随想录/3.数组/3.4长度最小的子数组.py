"""
Author: dpsfigo
Date: 2025-05-29 18:38:31
LastEditors: dpsfigo
LastEditTime: 2025-05-29 18:40:16
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/minimum-size-subarray-sum/
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
提示：

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""


class Solution:
    def minimum_size_subarray_sum(self, num: list[int], s: int) -> int:
        l = len(num)
        left = 0
        right = 0
        min_len = float("inf")
        cur_sum = 0
        while right < l:
            cur_sum += nums[right]
            while cur_sum >= s:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    sol = Solution()
    result = sol.minimum_size_subarray_sum(nums, s)
    print(result)
