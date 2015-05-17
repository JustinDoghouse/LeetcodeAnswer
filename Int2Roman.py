__author__ = 'burger'


class Solution:
    # @param num, an integer
    # @return a string
    def __init__(self):
        self.ele = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        self.roman = ''

    def intToRoman(self, num):
        a = num // 1000
        num -= a * 1000
        self.roman += 'M' * a
        i = 2
        while (i > -1):
            num = self.toRoman(num, i)
            i -= 1
        return self.roman

    def toRoman(self, num, level):
        # b = num//((10**level)*5)
        # num -= b;
        c = int(num // (10 ** level))
        if (c > 4):
            if (c == 9):
                self.roman += self.ele[level * 2] + self.ele[level * 2 + 2]
            else:
                self.roman += self.ele[level * 2 + 1] + self.ele[level * 2] * (c % 5)
        elif (c == 4):
            self.roman += self.ele[level * 2] + self.ele[level * 2 + 1]
        else:
            self.roman += self.ele[level * 2] * (c % 5)  # if __name__ =="__init__":
        return num - c * (10 ** level)


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(1000))


