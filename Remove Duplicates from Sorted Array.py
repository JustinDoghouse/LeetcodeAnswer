__author__ = 'burger'


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return None
        ns = ptr = 0
        while ns != len(A):
            while ns != len(A) - 1 and A[ns] == A[ns + 1]:
                ns += 1
            A[ptr] = A[ns]
            ptr += 1
            ns += 1
        return ptr


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))

