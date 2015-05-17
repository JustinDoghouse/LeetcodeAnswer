__author__ = 'burger'


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        ht = {}
        for i in range(len(num)):
            if ht.__contains__(target - num[i]):
                return (ht[target - num[i]] + 1, i + 1)
            else:
                ht[num[i]] = i


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([1, 2, 3], 4))