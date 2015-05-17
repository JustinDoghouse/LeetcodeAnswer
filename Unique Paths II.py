__author__ = 'burger'


class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        now = [1] + [0] * (m - 1)
        # for i in range(1,n):
        # if not obstacleGrid[i][0]:
        #         now[i] += now[i-1]

        for j in range(n):
            for i in range(m):
                if obstacleGrid[i][j]:
                    now[i] = 0
                else:
                    if i != 0:
                        now[i] += now[i - 1]
        return now[-1]


if __name__ == '__main__':
    s = Solution()
    g = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(s.uniquePathsWithObstacles(g))

