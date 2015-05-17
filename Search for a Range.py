__author__ = 'burger'


def schmid(num, tu, otr):
    tur = tu
    while (num[tur] != num[otr]):
        mid = (tur + otr) // 2
        if num[tur] == num[mid]:

            if tur == mid:
                return mid
            tur = mid
        else:
            if tur == mid + 1:
                return tur
            otr = mid
    return otr


def binearySearch(nums, target):
    lo = 0
    hi = len(nums) - 1
    while (lo <= hi):
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return lo, mid, hi
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo, -1, hi


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        lo, mid, hi, = binearySearch(nums, target)
        if mid == -1:
            return [-1, -1]
        else:
            lo = schmid(nums, mid, lo)
            hi = schmid(nums, mid, hi)
            return [lo, hi]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([0, 1, 1, 3, 3, 5, 5, 5, 6, 7, 7, 8, 8, 8, 9, 9, 10], 5))
