"""
Author: dpsfigo
Date: 2025-06-05 16:09:01
LastEditors: dpsfigo
LastEditTime: 2025-06-05 16:11:09
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/reverse-linked-list/
题意：反转一个单链表。

示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_linked_list(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre

            pre = cur
            cur = temp

        return pre


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    sol = Solution()
    ret = sol.reverse_linked_list(head)

    cur = ret
    while cur.next:
        print(cur.val)
        cur = cur.next
    print(cur.val)
