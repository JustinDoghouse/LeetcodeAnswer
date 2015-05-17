__author__ = 'burger'


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        contain = [[] for i in range(len(s))]
        i = -1
        while i < len(s):
            i += 1
            for j in range(i + 1, len(s) + 1):
                if wordDict.__contains__(s[i:j]):
                    contain[j - 1].append(i)
            while i < len(s) and not contain[i]:
                i += 1
        sentence = []
        for b in range(len(contain[-1])):
            sentence += print_word(contain, contain[-1][b], len(s) + 1, s)
        return sentence


def print_word(contain, i, j, s):
    ed = ''
    if j != len(contain) + 1:
        ed = ' '
    if not i:
        return [s[i:j] + ed]
    lst = []
    for b in range(len(contain[i - 1])):
        pre = print_word(contain, contain[i - 1][b], i, s)
        for a in range(len(pre)):
            lst.append(pre[a] + s[i:j] + ed)
    return lst


if __name__ == '__main__':
    slu = Solution()
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    s1 = "aaaaaaa"
    d1 = {"aaaa", "aa", "a"}
    lst = slu.wordBreak(s1, d1)
    print(lst)