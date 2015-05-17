__author__ = 'burger'

# TLE

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num) < 4:
            return []
        lst = []
        num.sort()
        for i in range(len(num) - 2):
            if i != 0 and num[i] == num[i - 1]:
                i += 1
            three = self.threeSum(num[i + 1:], target - num[i], num[i])
            if three == []:
                continue
            for j in range(len(three)):
                three[j][0] = num[i]
                lst.append(three[j])

        return lst

    def threeSum(self, num, tar, n0):
        lst = []
        for i in range(len(num) - 1):
            if i != 0 and num[i] == num[i - 1]:
                i += 1
            two = self.twoSum(num[i + 1:], tar - num[i])
            if two == []:
                continue
            for j in range(len(two)):
                two[j][0] = n0
                two[j][1] = num[i]
                lst.append(two[j])

        return lst

    def twoSum(self, num, tar1):
        lst = []
        l = 0
        r = len(num) - 1
        while l < r:
            if r + 1 != len(num) and num[r] == num[r + 1]:
                r -= 1
                continue
            if l != 0 and num[l] == num[l - 1]:
                l += 1
                continue
            if num[l] + num[r] > tar1:
                r -= 1
            elif num[l] + num[r] < tar1:
                l += 1
            else:
                lst.append([0, 0, num[l], num[r]])
                l += 1
                r -= 1
        return lst


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))