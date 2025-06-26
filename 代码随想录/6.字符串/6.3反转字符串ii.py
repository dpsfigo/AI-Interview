"""
Author: dpsfigo
Date: 2025-06-25 11:38:14
LastEditors: dpsfigo
LastEditTime: 2025-06-25 11:38:28
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/reverse-string-ii/

给定一个字符串 s 和一个整数 k，从字符串开头算起, 每计数至 2k 个字符，就反转这 2k 个字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。

如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"

"""


class Solution(object):
    def reverse_string_ii(self, s: str, k: int) -> str:
        def reverse_string(text):
            for i in range(int(len(text) // 2)):
                text[i], text[len(text) - 1 - i] = text[len(text) - 1 - i], text[i]
            return text

        res = list(s)

        for cur in range(0, len(res), 2 * k):
            res[cur : cur + k] = reverse_string(res[cur : cur + k])

        return "".join(res)


if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    sol = Solution()
    ret = sol.reverse_string_ii(s, k)
    print(ret)
