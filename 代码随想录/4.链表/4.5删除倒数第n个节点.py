"""
Author: dpsfigo
Date: 2025-06-09 19:11:12
LastEditors: dpsfigo
LastEditTime: 2025-06-09 19:25:05
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
输入：head = [1,2,3,4,5], n = 2 输出：[1,2,3,5]

示例 2：

输入：head = [1], n = 1 输出：[]

示例 3：

输入：head = [1,2], n = 1 输出：[1]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_node_from_end_of_list(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(0, head)
        slow = fast = dummy_head

        for i in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy_head.next
