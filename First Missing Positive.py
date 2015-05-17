__author__ = 'burger'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        has = 0
        for num in nums:
            if num > 0:
                has |= 1 << num
        for i in range(1, len(nums) + 1):
            has >>= 1
            if has % 2 == 0:
                return i
        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([]))

