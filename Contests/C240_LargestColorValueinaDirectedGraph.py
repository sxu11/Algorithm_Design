import copy


class Node():
    def __init__(self, c):
        self.color = c
        self.next = []
        self.prev = []
        # self.degree = 0


class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        nodes = dict()
        for i, color in enumerate(colors):
            node = Node(color)
            nodes[i] = node
        for i, j in edges:
            nodes[i].next.append(j)
            # nodes[i].degree += 1
            nodes[j].prev.append(i)
            # nodes[j].degree += 1
        q = []
        for i, node in nodes.items():
            if not node.prev:
                q.append(node)
        if not q:  # only detect 1 loop
            return -1
        # dfs
        # todo: can we have multiple sources?
        self.res = -1
        seen = dict()  # TODO: OK I don't know how to fully detect loop
        seenOnPath = set()  # I become to know right after contest...
        self.hasLoop = False

        def dfs(node, d, prevNode):
            # Wrong: return a dict, start from node, {color:cnt}
            # Right: pass prev {color:cnt} to this node, and pass to later
            # d = dict()
            if self.hasLoop:
                return
            if node in seenOnPath:
                self.hasLoop = True
                return
            seenOnPath.add(node)
            if node.color not in d:
                d[node.color] = 0
            d[node.color] += 1

            if not node.next:  # Time to calc
                maxCnt = max(d.values())
                if maxCnt > self.res:
                    self.res = maxCnt

            for nextNodeInd in node.next:
                nextNode = nodes[nextNodeInd]
                d_ = copy.deepcopy(d)
                dfs(nextNode, d, node)
                d = d_
            seenOnPath.remove(node)

        dfs(q[0], dict(), set())
        if self.hasLoop:
            return -1
        return self.res


