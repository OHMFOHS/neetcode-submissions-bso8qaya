class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        n = len(nums)
        visited = [False] * n
        def dfs(i):
            if len(path) == n:
                ans.append(path.copy())
                return
            for j in range(n):
                if visited[j]:
                    continue
                visited[j] = True
                path.append(nums[j])
                dfs(j + 1)
                visited[j] = False
                path.pop()
                
        dfs(0)
        return ans
