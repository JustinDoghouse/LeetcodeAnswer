__author__ = 'burger'


class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 1 or n == 0:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
