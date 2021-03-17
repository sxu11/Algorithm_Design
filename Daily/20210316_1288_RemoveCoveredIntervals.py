def isACoveredByB(a, b):
    return a[0] >= b[0] and a[1] <= b[1]


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        cntIntervals = len(intervals)
        cntToRemove = 0
        for i in range(cntIntervals):
            isCovered = 0
            for j in range(cntIntervals):
                if i == j:
                    continue
                if isACoveredByB(intervals[i], intervals[j]):
                    isCovered = 1
                    break
            cntToRemove += isCovered
        return cntIntervals - cntToRemove
