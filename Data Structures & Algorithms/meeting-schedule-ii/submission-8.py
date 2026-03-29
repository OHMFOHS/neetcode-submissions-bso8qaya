"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #sweep line
        mp = defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1
        cnt = 0
        ans = 0
        for t in sorted(mp):
            cnt += mp[t]
            ans = max(ans, cnt)
        return ans