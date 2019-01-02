
'''

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]

        def search_dfs(i, j):  # init state
            '''
            effect: set visited
            return: 1 or 0
            '''
            visited[i][j] = True
            if grid[i][j] == '0':
                return 0
            else:
                '''
                set 4 directions
                '''
                if i > 0 and not visited[i - 1][j]:
                    search_dfs(i - 1, j)
                if i < row - 1 and not visited[i + 1][j]:
                    search_dfs(i + 1, j)
                if j > 0 and not visited[i][j - 1]:
                    search_dfs(i, j - 1)
                if j < col - 1 and not visited[i][j + 1]:
                    search_dfs(i, j + 1)
                return 1

        tot_cnt = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j]:
                    tot_cnt += search_dfs(i, j)
        return tot_cnt


