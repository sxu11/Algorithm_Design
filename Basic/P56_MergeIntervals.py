'''

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals

        intvls = sorted(intervals, key=lambda x: x.start)
        i = 0
        while i < len(intvls) - 1:
            if intvls[i + 1].end <= intvls[i].end:
                intvls = intvls[:i + 1] + intvls[i + 2:] # TODO: easy to get wrong
            elif intvls[i + 1].start <= intvls[i].end:
                intvls[i].end = intvls[i + 1].end
                intvls = intvls[:i + 1] + intvls[i + 2:] # TODO: easy to get wrong
            else:
                i += 1
        return intvls


