class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        if n == 0:
            return [newInterval]

        for i in range(n):
            #newInterval is before the current interval
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
                #newInterval is behind the current interval
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            
        ans.append(newInterval)
        return ans
