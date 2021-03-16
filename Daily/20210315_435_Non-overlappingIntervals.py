# class Node:
#     def __init__(self, interval):
#         self.interval = interval
#         self.neighbors = []
#         self.degree = 0;

# def areTwoNodesLinked(node1, node2):
#     if node1.interval[0] >= node2.interval[1] or node1.interval[1] <= node2.interval[0]:
#         return False
#     else:
#         return True

# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         """
#         Thinking:
#         1. For each interval, find how many intervals are overlapped with it (like nodes "linked" in a graph)
#             - define Class
#         2. sort nodes by degree of links. Remove from the biggest (and de-link neighbors accordingly)
#             - use heap
#         3. util all degrees are 0.
#         """
#         nodes = []
#         for interval in intervals:
#             node = Node(interval)
#             nodes.append(node)

#         numNodes = len(nodes)
#         inds = []
#         for i in range(numNodes):
#             for j in range(i+1, numNodes):
#                 if areTwoNodesLinked(nodes[i], nodes[j]):
#                     nodes[i].neighbors.append(nodes[j])
#                     nodes[i].degree += 1
#                     nodes[j].neighbors.append(nodes[i])
#                     nodes[j].degree += 1
#             if nodes[i].degree > 0:
#                 heapq.heappush(inds, (-nodes[i].degree, i))

#         res = 0
#         while inds != []:
#             negaMaxDegree, ind = heapq.heappop(inds)
#             res += 1

#             newNum0s = 0
#             for node in nodes[ind].neighbors:
#                 node.degree -= 1
#                 if node.degree == 0:
#                     newNum0s += 1
#             if newNum0s == len(inds):
#                 break
#         return res

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        intervals_sorted = sorted(intervals, key=lambda interval: interval[1])
        totalCnt = len(intervals_sorted)

        cntNonOverlap = 1
        curEnd = intervals_sorted[0][1]
        for i in range(1, totalCnt):
            if intervals_sorted[i][0] >= curEnd:
                cntNonOverlap += 1
                curEnd = intervals_sorted[i][1]
        return totalCnt - cntNonOverlap
