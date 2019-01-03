
'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.

'''


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        # Init a dict of receive_times
        receive_time = {}
        for i in range(1, N + 1):
            receive_time[i] = float('inf')
        receive_time[K] = 0

        edge = {}
        for time in times:
            v, u, w = time
            if v in edge:
                edge[v].append((u, w))
            else:
                edge[v] = [(u, w)]

        from heapq import heappush, heappop
        queue = [(0, K)]
        seen = set()

        while queue:
            t, v = heappop(queue)
            seen.add(v)

            # update receive_times
            # for time in times:
            if v in edge:
                for u, w in edge[v]:
                    # if time[0] == v:
                    receive_time[u] = min(receive_time[u], t + w)
                    if not (u in seen):
                        # add neighboring v's
                        heappush(queue, (receive_time[u], u))
        max_t = max(receive_time.values())

        if max_t == float('inf'):
            return -1
        else:
            return max_t



