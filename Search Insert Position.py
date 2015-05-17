__author__ = 'burger'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        while (lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([0, 1, 3, 5, 6, 7, 8, 9, 10], 11))