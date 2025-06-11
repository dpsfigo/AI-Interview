"""
Author: dpsfigo
Date: 2025-06-11 13:39:12
LastEditors: dpsfigo
LastEditTime: 2025-06-11 14:24:54
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/linked-list-cycle-ii/
题意： 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def linked_list_cycle_ii(self, head: ListNone) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # 快慢指针法，x=z
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None
