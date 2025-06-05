"""
Author: dpsfigo
Date: 2025-06-05 11:29:17
LastEditors: dpsfigo
LastEditTime: 2025-06-05 11:36:14
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/remove-linked-list-elements/
题意：删除链表中等于给定值 val 的所有节点。

示例 1： 输入：head = [1,2,6,3,4,5,6], val = 6 输出：[1,2,3,4,5]

示例 2： 输入：head = [], val = 1 输出：[]

示例 3： 输入：head = [7,7,7,7], val = 7 输出：[]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_linked_list_elements(
        self, held: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        # 增加一个虚拟头节点
        dummy_head = ListNode(next=head)

        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy_head.next


if __name__ == "__main__":
    # 构建测试链表: [1,2,6,3,4,5,6]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)

    # 创建解决方案实例
    sol = Solution()

    # 测试删除值为6的节点
    result = sol.remove_linked_list_elements(head, 6)

    # 打印结果链表
    current = result
    while current:
        print(current.val, end=" ")
        current = current.next
    print()  # 换行
