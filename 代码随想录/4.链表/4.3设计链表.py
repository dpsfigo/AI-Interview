"""
Author: dpsfigo
Date: 2025-06-05 13:23:12
LastEditors: dpsfigo
LastEditTime: 2025-06-05 13:23:26
Description: 请填写简介
"""

"""
在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
https://file1.kamacoder.com/i/algo/20200814200558953.png
"""


# 单链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.dummy_head.next
        for i in range(index):
            current = current.next

        return current

    def add_at_head(self, val):
        self.dummy_head.next = ListNode(self.dummy_head.next, val)
        self.size += 1

    def add_at_tail(self, val):
        current = self.dummy_head
        for i in range(self.size):
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def add_at_index(self, index: int, val: int):
        if index > self.size or index < 0:
            return

        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def delete_at_index(self, index):
        if index >= self.size or index < 0:
            return

        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


if __name__ == "__main__":
    # 创建链表实例
    linked_list = MyLinkedList()

    # 测试添加节点
    linked_list.add_at_head(1)  # 链表变为 1
    linked_list.add_at_tail(3)  # 链表变为 1->3
    linked_list.add_at_index(1, 2)  # 链表变为 1->2->3

    # 测试获取节点值
    print(linked_list.get(1))  # 应该输出 2

    # 测试删除节点
    linked_list.delete_at_index(1)  # 链表变为 1->3

    # 测试获取节点值
    print(linked_list.get(1))  # 应该输出 3
