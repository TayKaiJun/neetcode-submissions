"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: ( x.start, x.end ) )
        # store the latest ending time of each room
        rooms = []
        for interval in intervals:
            start = interval.start
            end = interval.end

            found = False
            for i in range(len(rooms)):
                if start >= rooms[i]:
                    rooms[i] = end
                    found = True
                    break
            if not found:
                rooms.append(end)

        return len(rooms)