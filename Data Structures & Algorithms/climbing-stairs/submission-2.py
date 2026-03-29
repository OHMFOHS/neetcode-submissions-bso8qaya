class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        f1 = 1
        f2 = 1
        for i in range(n - 1):
            temp = f2
            f2 = f1 + f2
            f1 = temp
        return f2
