__author__ = 'burger'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        n = len(nums)
        contain = [0] * n
        # ncon = [0] * n
        # l = [0] * n
        contain[0] = nums[0]
        # ncon[0] = max(nums[0],0)
        # l[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i] + contain[i - 1]:
                contain[i] = nums[i]
                #        l[i] = 1
            else:
                contain[i] = nums[i] + contain[i - 1]
        #         l[i] = l[i - 1] + 1
        #idx,val = max(enumerate(l),key = operator.itemgetter(1))
        return max(contain)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))