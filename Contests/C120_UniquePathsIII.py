'''
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation:
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.


Note:

1 <= grid.length * grid[0].length <= 20
'''


class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])

        q = [[0, 0]]
        visited = [[False] * col for _ in range(row)]

        num_0s = 0
        for i in range(row):
            for j in range(col):
                num_0s += (grid[i][j] == 0)
                if grid[i][j] == 1:
                    start = [i, j]

        res = 0
        seen_0s = 0

        def dfs(n, res, seen_0s, visited):
            # print n
            if grid[n[0]][n[1]] == 2:
                # make a decision
                # print seen_0s, num_0s
                if seen_0s == num_0s:
                    res += 1
                    return res, seen_0s, visited
                else:
                    return res, seen_0s, visited
            elif grid[n[0]][n[1]] == -1:
                # go back
                visited[n[0]][n[1]] = True
                return res, seen_0s, visited
            else:
                if grid[n[0]][n[1]] == 0:
                    seen_0s += 1
                visited[n[0]][n[1]] = True

                if n[0] - 1 >= 0 and not visited[n[0] - 1][n[1]]:
                    res, seen_0s, visited = dfs([n[0] - 1, n[1]], res, seen_0s, visited)
                if n[0] + 1 < row and not visited[n[0] + 1][n[1]]:
                    res, seen_0s, visited = dfs([n[0] + 1, n[1]], res, seen_0s, visited)
                if n[1] - 1 >= 0 and not visited[n[0]][n[1] - 1]:
                    res, seen_0s, visited = dfs([n[0], n[1] - 1], res, seen_0s, visited)
                if n[1] + 1 < col and not visited[n[0]][n[1] + 1]:
                    res, seen_0s, visited = dfs([n[0], n[1] + 1], res, seen_0s, visited)
                visited[n[0]][n[1]] = False
                seen_0s -= 1
                return res, seen_0s, visited

        res, seen_0s, visited = dfs(start, res, seen_0s, visited)
        return res





