__author__ = 'burger'


class Solution:
    # @param s, a string
    # @return a boolean
    def isValid_clear_code_from_web(self, s):
        paren_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for p in s:
            if p in paren_map:
                stack.append(paren_map[p])
            else:
                if not stack or stack.pop() != p:
                    return False

        return not stack

    def isValid(self, s):
        pair = {'(': 0, ')': 1, '{': 2, '}': 3, '[': 4, ']': 5}
        list = []
        for char in s:
            if pair[char] % 2 == 0:
                list.append(char)
            elif len(list) != 0:
                if not pair[list.pop()] == pair[char] - 1:
                    return False
            else:
                return False
        if len(list) != 0:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("("))
