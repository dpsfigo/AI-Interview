"""
Author: dpsfigo
Date: 2025-05-30 16:47:19
LastEditors: dpsfigo
LastEditTime: 2025-06-03 17:48:56
Description: 请填写简介
"""

"""
https://leetcode.cn/problems/spiral-matrix-ii/
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
示例:
输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]
"""


class Solution:
    def spiral_matrix_ii_v1(self, n: int) -> list:
        nums = [[0] * n for _ in range(n)]
        start_x, start_y = 0, 0
        loop, mid = n // 2, n // 2
        count = 1
        for offset in range(1, loop + 1):
            for i in range(start_y, n - offset):  # 从左到右
                nums[start_x][i] = count
                count += 1
            for i in range(start_x, n - offset):  # 从上到下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, start_y, -1):  # 从右到左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, start_x, -1):  # 从下到上
                nums[i][start_y] = count
                count += 1

            start_x += 1
            start_y += 1

        if n % 2 != 0:
            nums[mid][mid] = count
        return nums

    def spiral_matrix_ii(self, n: int) -> list:
        left, top, right, bottom = 0, 0, n - 1, n - 1
        nums = [[0] * n for _ in range(n)]
        count = 1
        while count <= n * n:
            # 向右
            for j in range(left, right + 1, 1):
                nums[top][j] = count
                count += 1
            # 向下
            top += 1
            for i in range(top, bottom + 1, 1):
                nums[i][right] = count
                count += 1

            right -= 1
            # 向左
            for j in range(right, left - 1, -1):
                nums[bottom][j] = count
                count += 1

            bottom -= 1
            # 向上

            for i in range(bottom, top - 1, -1):
                nums[i][left] = count
                count += 1

            left += 1

        return nums


if __name__ == "__main__":
    n = 3
    sol = Solution()
    ret = sol.spiral_matrix_ii(n)
    print(ret)
