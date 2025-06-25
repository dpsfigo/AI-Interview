"""
Author: dpsfigo
Date: 2025-06-25 10:53:54
LastEditors: dpsfigo
LastEditTime: 2025-06-25 11:03:46
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/reverse-string/
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

示例 2：
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""


class Solution(object):
    def reverse_string(self, input: str) -> str:
        for i in range(int(len(input) // 2)):
            input[i], input[len(input) - 1 - i] = input[len(input) - 1 - i], input[i]
        return input


if __name__ == "__main__":
    input = ["H", "a", "n", "n", "a", "h"]
    sol = Solution()
    ret = sol.reverse_string(input)
    print(ret)
