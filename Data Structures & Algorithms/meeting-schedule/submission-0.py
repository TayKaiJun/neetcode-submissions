"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        lastEnd = 0
        for meet in intervals:
            start = meet.start
            end = meet.end
            if start < lastEnd:
                return False
            lastEnd = end
        return True