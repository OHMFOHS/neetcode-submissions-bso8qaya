"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
            
        intervals.sort(key = lambda x : x.start)
        room = []
        
        for i in range(n):
            if room:
                if intervals[i].start >= room[0]:
                    heapq.heappop(room)
                    heapq.heappush(room, intervals[i].end)
                else:
                    heapq.heappush(room, intervals[i].end)
            else:
                heapq.heappush(room, intervals[i].end)
        return len(room)