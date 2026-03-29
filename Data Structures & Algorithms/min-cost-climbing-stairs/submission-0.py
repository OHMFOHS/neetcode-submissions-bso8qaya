class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        f1 = f2 = 0
        for i in range(2, n + 1):
            temp = f2
            f2 = min(f1 + cost[i-2], f2 + cost[i-1])
            f1 = temp
        return f2