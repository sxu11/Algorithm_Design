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


