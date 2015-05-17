__author__ = 'burger'


class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        now = [1] * m
        n -= 1
        while n:
            for i in range(1, m):
                now[i] += now[i - 1]
            n -= 1
        return now[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
