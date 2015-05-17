__author__ = 'burger'


class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        # result = ['1']
        result = '1'

        for i in range(n - 1):
            count = 1
            tmp = ''
            pre = ''
            for x in result:
                if pre:
                    if pre == x:
                        count += 1
                    else:
                        tmp += str(count) + pre
                        count = 1
                        pre = x
                else:
                    pre = x
            result = tmp + str(count) + pre
        return result


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        print(s.countAndSay(i))

        # 1 11 21 1211 111221 312211 13112221
