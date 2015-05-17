__author__ = 'burger'


class Solution:
    # @param digits, a string
    # @return a string[]
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        mapDtoL = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        sary = []
        self.lc(digits, mapDtoL, '', sary)
        return sary

    def lc(self, digits, mdl, str, sary):
        for l in mdl[digits[0]]:
            nstr = str + l
            if len(digits) == 1:
                sary.append(nstr)
            else:
                self.lc(digits[1:], mdl, nstr, sary)


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations(""))