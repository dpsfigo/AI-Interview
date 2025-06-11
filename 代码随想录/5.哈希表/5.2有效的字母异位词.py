"""
Author: dpsfigo
Date: 2025-06-11 16:43:28
LastEditors: dpsfigo
LastEditTime: 2025-06-11 16:48:26
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/valid-anagram/

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1: 输入: s = "anagram", t = "nagaram" 输出: true

示例 2: 输入: s = "rat", t = "car" 输出: false

说明: 你可以假设字符串只包含小写字母。
"""


class Solution:
    def valid_anagram(s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            record[ord(i) - ord("a")] += 1

        for i in t:
            record[ord(i) - ord("a")] -= 1

        for i in record:
            if i != 0:
                return False
        return True


if __name__ == "__main__":
    s = "tea"
    t = "eats"
    sol = Solution
    ret = sol.valid_anagram(s, t)
    print(ret)
