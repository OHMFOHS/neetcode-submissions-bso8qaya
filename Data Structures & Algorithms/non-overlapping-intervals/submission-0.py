
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        def dfs(i, prev):
            if i == len(intervals):
                return 0
            #不选当前的 interval
            res = dfs(i+1, prev)

            #如果不重叠，选当前interval
            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                res = max(res, 1 + dfs(i + 1, i))
            return res
        return len(intervals) - dfs(0, -1)