__author__ = 'burger'


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        return search(s, p, 0, 0)


def search(s, p, i, j):
    if i == len(s):
        if j == len(p) or (j == len(p) - 1 and p[j] == '*'):
            return True
        else:
            return False
    if j == len(p):
        return False
    if s[i] == p[j] or p[j] == '.':
        return search(s, p, i + 1, j + 1)

    if p[j] == '*':
        return search(s, p, i, j - 1) or search(s, p, i, j + 1)
    if j != len(p) - 1 and p[j + 1] == '*':
        return search(s, p, i, j + 1)
    return False


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("aa", "c*a*b"))
