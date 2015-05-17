__author__ = 'burger'


def gp(str, n, stack):
    lst = []
    if n == 0:
        return [str + ')' * stack]
    if stack == 0:
        return gp(str + '(', n - 1, stack + 1)
    else:
        return gp(str + '(', n - 1, stack + 1) + gp(str + ')', n, stack - 1)


class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        return gp('', n, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(1))


