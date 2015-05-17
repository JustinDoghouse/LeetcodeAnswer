__author__ = 'burger'


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            tmp = self.permute(nums[:i] + nums[i + 1:])
            for x in tmp:
                x.append(nums[i])
                result.append(x)
        return result


if __name__ == '__main__':
    s = Solution()
    for i in s.permute([1, 2, 3]):
        for j in i:
            print(j)
