__author__ = 'burger'


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        # return search(s, p, 0, 0)
        return dp(s, p)


# reference: https://leetcode.com/discuss/22743/python-dp-solution
def dp(s, p):
    l = len(s)
    if len(p) - p.count('*') > l:
        return False
    dp = [True] + [False] * l
    for char in p:
        ndp = [dp[0] and char == '*']
        if char == '*':
            for i in range(l):
                ndp += [ndp[-1] or dp[i + 1]]
        elif char == '?':
            ndp += dp[:l]
        else:
            ndp += [s[j] == char and dp[j] for j in range(l)]
        dp = ndp
    return dp[-1]


if __name__ == '__main__':
    s = Solution()
    a1 = "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb"
    b1 = "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"
    a2 = "abc"
    b2 = "a*"
    a3 = "aaaaa"
    b3 = "*?aa*"
    a4 = "aabb"
    a5 = 'aab'
    b5 = 'c*a*b'
    print(s.isMatch(a1, b1))


def dp_messed_up(s, p):
    l = len(s)
    if not s:
        if len(p) - p.count('*') == 0:
            return True
        return False
    if not p:
        return False
    if len(p) - p.count('*') > l:
        return False
    if p[0] == '*':
        dp = [True] * l
    else:
        dp = [s[0] == p[0] or p[0] == '?'] + [False] * (l - 1)

    for j in range(1, len(p)):
        char = p[j]
        if char == '*':
            for i in range(1, l):
                dp[i] = dp[i] or dp[i - 1]
        else:
            for i in range(l - 1, 0, -1):
                dp[i] = dp[i - 1] and (s[i] == char or char == '?')
            dp[0] = (s[0] == char or char == '?') and dp[0]
    return dp[-1]


#reference: http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html
def yucoding(s, p):
    sposi = 0
    pposi = 0
    slst = 0
    star = -1
    while sposi < len(s):
        if pposi < len(p) and (p[pposi] == '?' or p[pposi] == s[sposi]):
            pposi += 1
            sposi += 1
        elif pposi < len(p) and p[pposi] == '*':
            star = pposi
            pposi += 1
            slst = sposi
        elif star != -1:
            pposi = star + 1
            slst += 1
            sposi = slst
        else:
            return False
    while pposi < len(p) and p[pposi] == '*':
        pposi += 1
    if pposi == len(p):
        return True
    else:
        return False


#TLE
def find(s, i, pj):
    lst = []
    for ii in range(i, len(s)):
        if s[ii] == pj:
            lst.append(ii)
    return lst


#TLE
def search(s, i, p, j):
    if i == len(s):
        if j == len(p):
            return True
        while p[j] == '*':
            j += 1
            if j == len(p):
                return True
        return False
    if j == len(p):
        return False
    if p[j] == s[i] or p[j] == '?':
        return search(s, i + 1, p, j + 1)
    if p[j] == '*':
        while p[j] == '*':
            j += 1
            if j == len(p):
                return True
        lst = find(s, i, p[j])
        while lst:
            if (search(s, lst.pop() + 1, p, j + 1)):
                return True
    return False

#TLE
# def search(s,p,i,j):
#     if i == len(s):
#         if j == len(p):
#             return True
#         else:
#             return False
#     if j == len(p):
#         return False
#     if s[i] == p[j] or p[j] == '?':
#         return search(s,p,i+1,j+1)
#     if p[j] =='*':
#         while p[j] == '*':
#             j += 1
#         for()
#     return False

