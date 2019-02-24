
'''
On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.

Initially, some number of lamps are on.  lamps[i] tells us the location of the i-th lamp that is on.  Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

For the i-th query queries[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.

After each query (x, y) [in the order given by queries], we turn off any lamps that are at cell (x, y) or are adjacent 8-directionally (ie., share a corner or edge with cell (x, y).)

Return an array of answers.  Each value answer[i] should be equal to the answer of the i-th query queries[i].



Example 1:

Input: N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation:
Before performing the first query we have both lamps [0,0] and [4,4] on.
The grid representing which cells are lit looks like this, where [0,0] is the top left corner, and [4,4] is the bottom right corner:
1 1 1 1 1
1 1 0 0 1
1 0 1 0 1
1 0 0 1 1
1 1 1 1 1
Then the query at [1, 1] returns 1 because the cell is lit.  After this query, the lamp at [0, 0] turns off, and the grid now looks like this:
1 0 0 0 1
0 1 0 0 1
0 0 1 0 1
0 0 0 1 1
1 1 1 1 1
Before performing the second query we have only the lamp [4,4] on.  Now the query at [1,0] returns 0, because the cell is no longer lit.


Note:

1 <= N <= 10^9
0 <= lamps.length <= 20000
0 <= queries.length <= 20000
lamps[i].length == queries[i].length == 2
'''


class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # horizons = [False]*N
        # verticals = [False]*N
        # trendups = [False]*(N*2)
        # trenddowns = [False]*(N*2)
        from collections import Counter
        h = Counter()
        v = Counter()
        diff = Counter()
        summ = Counter()

        lamps_set = set()
        for lamp in lamps:
            h[lamp[0]] += 1
            v[lamp[1]] += 1
            diff[lamp[1] - lamp[0]] += 1
            summ[lamp[0] + lamp[1]] += 1

            lamps_set.add(tuple(lamp))
            # horizons[lamp[0]] = True
            # verticals[lamp[1]] = True
            # trendups[lamp[1]-lamp[0]+N] = True
            # trenddowns[lamp[0]-lamp[1]+N] = True

        def turn_off(i, j):
            if i < 0 or i >= N or j < 0 or j >= N:
                return
            # horizons[i] = False
            # verticals[j] = False
            # trendups[j-i+N] = False
            # trenddowns[i-j+N] = False
            if (i, j) not in lamps_set:
                return
            h[i] -= 1
            v[j] -= 1
            diff[j - i] -= 1
            summ[i + j] -= 1

        # lamps_set = set(lamps)
        # print  h
        # print v
        # print diff
        # print summ
        res = []
        for query in queries:
            if (h[query[0]] > 0) or (v[query[1]] > 0) or (diff[query[1] - query[0]] > 0) or (
                    summ[query[0] + query[1]] > 0):
                res.append(1)
            else:
                res.append(0)
            turn_off(query[0], query[1])
            turn_off(query[0] - 1, query[1])
            turn_off(query[0] + 1, query[1])
            turn_off(query[0], query[1] - 1)
            turn_off(query[0], query[1] + 1)
            turn_off(query[0] - 1, query[1] - 1)
            turn_off(query[0] + 1, query[1] + 1)
            turn_off(query[0] + 1, query[1] - 1)
            turn_off(query[0] - 1, query[1] + 1)

            # print  h
            # print v
            # print diff
            # print summ
        return res

