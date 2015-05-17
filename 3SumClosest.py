__author__ = 'burger'


class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        sum = num[0] + num[1] + num[2]
        for i in range(len(num) - 1):
            j = i + 1
            k = len(num) - 1
            while j < k:
                tmp = num[i] + num[j] + num[k]
                if tmp == target:
                    return target
                if abs(tmp - target) < abs(sum - target):
                    sum = tmp
                if tmp < target:
                    j += 1
                else:
                    k -= 1
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-3, -2, -5, 3, -4], -1))