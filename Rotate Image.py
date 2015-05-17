__author__ = 'burger'


class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(n // 2):
                tmp = 0
                x = i
                y = j
                xt = y
                yt = n - x - 1
                last = matrix[x][y]
                for l in range(4):
                    tmp = matrix[xt][yt]
                    matrix[xt][yt] = last
                    x = yt
                    y = n - xt - 1
                    xt = x
                    yt = y
                    last = tmp


if __name__ == '__main__':
    s = Solution()
    n = [[1, 2], [3, 4]]
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(n)
    print(n)
