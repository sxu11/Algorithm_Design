
'''

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        times = {}
        for interval in intervals:
            if interval.start in times:
                times[interval.start].append('start')
            else:
                times[interval.start] = ['start']

            if interval.end in times:
                times[interval.end].append('end')
            else:
                times[interval.end] = ['end']

        num_rooms = 0
        max_room_required = 0
        for key in sorted(times.keys()):
            vals = times[key]
            for val in vals:
                if val == 'start':
                    num_rooms += 1
                else:
                    num_rooms -= 1

            max_room_required = max(max_room_required, num_rooms) #TODO: put here is right!
        return max_room_required


