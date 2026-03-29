class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            if cur_interval[0] <= ans[-1][1]:
                ans[-1][1] = max(cur_interval[1], ans[-1][1])
            else:
                ans.append(cur_interval)
        return ans

