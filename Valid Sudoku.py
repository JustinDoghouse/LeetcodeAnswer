__author__ = 'burger'


class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        col = [set() for x in range(9)]
        square = [set() for x in range(9)]
        for i in range(9):
            row = set()
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if not row.__contains__(val) and not col[j].__contains__(val) and not square[
                                        i - i % 3 + j // 3].__contains__(val):
                        square[i - i % 3 + j // 3].add(val)
                        row.add(val)
                        col[j].add(val)
                    else:
                        return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku(
        [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
         "9........"]
    ))


