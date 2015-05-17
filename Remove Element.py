__author__ = 'burger'


class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if not A:
            return None
        ns = ptr = 0
        while ns < len(A):
            while ns != len(A) and A[ns] == elem:
                ns += 1
            if ns == len(A):
                break
            A[ptr] = A[ns]
            ptr += 1
            ns += 1
        return ptr


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([5, 6], 5))
