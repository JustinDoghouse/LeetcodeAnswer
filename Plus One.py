__author__ = 'burger'


class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):

        for i in range(len(digits) - 1, - 1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                if i == 0 and digits[i] == 0:
                    digits.insert(0, 1)
                    return digits
            else:
                return digits