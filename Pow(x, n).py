__author__ = 'burger'


class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0: return 1
        if x == 0: return 0
        if n < 0: return 1 / self.myPow(x, -n)

        i = 1
        tmp = x
        while n > i * 2:
            tmp *= tmp
            i *= 2
        return tmp * self.myPow(x, n - i)


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(34.00515, -3))