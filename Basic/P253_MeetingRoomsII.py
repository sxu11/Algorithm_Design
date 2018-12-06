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


