"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1
        cnt = 0
        ans = 0
        for time in sorted(mp):
            cnt += mp[time]
            ans = max(ans, cnt)
        return ans