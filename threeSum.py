__author__ = 'burger'


class Solution:
    def threeSum(self, num):
        if len(num) < 3:
            return []
        lst = []
        num.sort()
        ti = len(num) - 1
        target = -num[ti]

        while target <= 0 and ti > 1:
            if ti != len(num) - 1 and num[ti] == num[ti + 1]:
                ti -= 1
                continue
            target = -num[ti]
            l = 0
            r = ti - 1
            while l < r:
                if r + 1 != ti and num[r] == num[r + 1]:
                    r -= 1
                    continue
                if l != 0 and num[l] == num[l - 1]:
                    l += 1
                    continue
                if num[l] + num[r] > target:
                    r -= 1
                elif num[l] + num[r] < target:
                    l += 1
                else:
                    lst.append([num[l], num[r], -target])
                    l += 1
                    r -= 1
            ti -= 1

        return lst


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([0, 0, 0, 0, 1, 1, -1, -1, 1]))