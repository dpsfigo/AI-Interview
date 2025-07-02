"""
Author: dpsfigo
Date: 2025-07-01 14:52:18
LastEditors: dpsfigo
LastEditTime: 2025-07-01 17:29:32
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/implement-stack-using-queues/

使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())

        self.queue_in, self.queue_out = self.queue_out, self.queue_in

        return self.queue_out.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue_in[-1]

    def empty(self) -> bool:
        return len(self.queue_in) == 0


if __name__ == "__main__":
    sol = MyStack()
    sol.push(1)
    sol.push(2)
    sol.push(3)
    ret = sol.top()
    print(ret)
    ret = sol.pop()
    print(ret)
    ret = sol.empty()
    print(ret)
