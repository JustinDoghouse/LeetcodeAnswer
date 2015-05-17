__author__ = 'burger'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        doit = 0
        notdo = 0
        for pri in nums:
            tmp = doit
            doit = notdo + pri
            notdo = max(notdo, tmp)
        return max(doit, notdo)


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 4, 5]))
