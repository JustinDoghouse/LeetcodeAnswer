__author__ = 'burger'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        lo = 0
        le = len(nums)
        hi = le - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[lo]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                break
        start = lo
        # ---------finding target-----------
        lo = 0
        hi = le - 1
        while (lo <= hi):
            mid = (lo + hi) // 2
            rm = (start + mid) % le
            if nums[rm] == target:
                return rm
            elif nums[rm] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([3, 6, 90, -5, 0, 1, 2], -5))

