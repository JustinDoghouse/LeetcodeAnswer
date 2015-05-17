__author__ = 'burger'


class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[m + n + 1] = nums1[m]
                m -= 1
            else:
                nums1[m + n + 1] = nums2[n]
                n -= 1
        if n >= 0:
            nums1[:n + 1] = nums2[:n + 1]


if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 4, 0, 0, 0]
    s.merge(a, 4, [2, 5, 7], 3)
    print(a)

