class Solution:
    def climbStairs(self, n: int) -> int:
        #这里没有dfs(n) 这个状态，所以可以就 n 的长度
        cache = [-1] * n
        def dfs(i):
            #刚好到第 n 阶 → 1 种合法走法,走过头（超过 n） → 0 种走法
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        return dfs(0)