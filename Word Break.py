__author__ = 'burger'


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        contain = [False] * len(s)
        i = -1
        while i < len(s):
            i += 1
            for j in range(i + 1, len(s) + 1):
                if wordDict.__contains__(s[i:j]):
                    contain[j - 1] = True
            while i < len(s) and not contain[i]:
                i += 1
        return contain[-1]


if __name__ == '__main__':
    s = "leetcode"
    dict = {"leet", "code"}
    a = 'ab'
    d = {'a', 'b'}
    slu = Solution()
    print(slu.wordBreak(a, d))