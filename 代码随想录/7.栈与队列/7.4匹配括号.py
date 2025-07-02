"""
Author: dpsfigo
Date: 2025-07-02 16:20:06
LastEditors: dpsfigo
LastEditTime: 2025-07-02 16:20:22
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/valid-parentheses/

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
#
"""


class Solution:
    def vaild_parentheses(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == "(":
                stack.append(")")
            elif item == "[":
                stack.append("]")
            elif item == "{":
                stack.append("}")
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()

        return True if not stack else False
