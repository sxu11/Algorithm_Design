class Node():
    def __init__(self):
        self.tag = -1
        self.neighbors = []
        self.weights = []


class Solution:
    # def dfs(self):
    #     """
    #     dfs until reaching the sink
    #       - don't revisit nodes
    #     mark nodes on path visited
    #       - when reaching the sink, numPath +1
    #     after dfs a direction,
    #     """
    def __init__(self):
        self.dists = None
        self.res = 0
        self.n = -1
        self.nodes = None

    def dfs(self, node):
        # print(node)
        # print(node.tag)
        if node.tag == self.n:
            self.res += 1
        else:
            for neighbor in node.neighbors:
                if self.dists[node.tag] > self.dists[neighbor]:
                    self.dfs(self.nodes[neighbor])

    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # set up
        self.n = n

        self.nodes = dict()
        for i in range(1, n + 1):
            node = Node()
            node.tag = i
            self.nodes[i] = (node)

        for edge in edges:
            node1 = self.nodes[edge[0]]
            node2 = self.nodes[edge[1]]

            node1.neighbors.append(edge[1])
            node1.weights.append(edge[2])

            node2.neighbors.append(edge[0])
            node2.weights.append(edge[2])

        #         # 1st pass, bfs, compute all distances

        #         dists = dict()
        #         q = [nodes[1]]
        #         visited = set()
        #         while len(q) > 0:
        #             curNode = q[0]

        #             if curNode.tag == n:
        #                 """TODO: reached sink"""
        #             else:

        maxnum = float("inf")
        # Dijkstra
        dist = dict()
        # prev = dict()
        Q = []
        for i in range(1, n + 1):
            dist[i] = maxnum
            # prev[i] = None
            Q.append(i)
        dist[n] = 0

        while len(Q) > 0:
            u = Q[0]
            for q in Q:
                if dist[q] < dist[u]:
                    u = q
            Q.remove(u)

            for i in range(len(self.nodes[u].neighbors)):
                neighbor = self.nodes[u].neighbors[i]
                if neighbor not in Q:
                    continue
                alt = dist[u] + self.nodes[u].weights[i]
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    # prev[i] = u
        # print(dist)

        self.dists = dist

        # 2nd pass, dfs,
        self.dfs(self.nodes[1])
        return self.res
