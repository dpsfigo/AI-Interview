"""
Author: dpsfigo
Date: 2025-06-26 14:25:35
LastEditors: dpsfigo
LastEditTime: 2025-06-26 14:34:20
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/reverse-words-in-a-string/

给定一个字符串，逐个翻转字符串中的每个单词。

示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""


class Solution(object):
    def reverse_words_in_a_string(self, s: str) -> str:
        s = s[::-1]
        return " ".join(word[::-1] for word in s.split())


if __name__ == "__main__":
    s = "the sky is blue"
    sol = Solution()
    ret = sol.reverse_words_in_a_string(s)
    print(ret)
