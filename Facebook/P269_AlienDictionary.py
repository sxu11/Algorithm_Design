from collections import deque


class Node:
    def __init__(self, alp):
        self.alp = alp
        self.asc = set()
        self.des = set()  # only key

    def getIndegree(self):
        return len(self.asc)


class Solution:
    def extract2Words(self, word1, word2):
        minLen = min(len(word1), len(word2))
        for i in range(minLen):
            if word1[i] != word2[i]:
                return (word1[i], word2[i])

        if len(word1) <= len(word2):  # no info
            return -1
        else:  # wrong
            return None

    def alienOrder(self, words: List[str]) -> str:
        """ step 1,2: collect data"""
        """ step 1: one-word-wise info extraction"""
        allNodes = dict()

        for word in words:
            for j in range(0, len(word)):
                if word[j] not in allNodes:
                    allNodes[word[j]] = Node(word[j])

                """
                if j < len(word)-1 and word[j]!=word[j+1]:
                    allNodes[word[j]].des.add(word[j+1])
                if j > 0 and word[j]!=word[j-1]:
                    allNodes[word[j]].asc.add(word[j-1])
                """
        # for alp,node in allNodes.items():
        # print(alp, node.alp, node.asc, node.des)

        """ step 2: two-word-wise info extract"""
        for i in range(len(words) - 1):
            pair = self.extract2Words(words[i], words[i + 1])
            if pair is None:
                return ""
            if pair != -1:
                allNodes[pair[1]].asc.add(pair[0])
                allNodes[pair[0]].des.add(pair[1])
                # print("pair:", pair)

        """ step 3: topological sort
        if there is a loop, fail
        """
        curCnt = 0
        alpCnt = len(allNodes)
        res = ""
        q = deque()  # deque([words[0][0]]) # use deque
        for alp in allNodes:
            if allNodes[alp].getIndegree() == 0:
                q.append(alp)

        while curCnt < alpCnt:  # q:
            # print(q)
            if not q:
                return ""

            alp = q.popleft()
            # if alp in res or allNodes[alp].getIndegree()>0:
            # return ""
            res += alp
            curCnt += 1
            # if alp=="r":
            # print("allNodes[alp].des",allNodes[alp].des)

            for des in allNodes[alp].des:
                if alp not in allNodes[des].asc:
                    return ""
                allNodes[des].asc.remove(alp)
                if allNodes[des].getIndegree() == 0:
                    q.append(des)
        return res