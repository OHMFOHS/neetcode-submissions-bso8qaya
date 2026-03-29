class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        path = []
        ans = []
        candidates.sort()
        visited = [False] * n
        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return
            if i == n or candidates[i] > left:
                return
            for j in range(i, n):
                if j > 0 and candidates[j] == candidates[j-1] and not visited[j-1] :
                    continue
                path.append(candidates[j])
                visited[j] = True
                dfs(j + 1, left - candidates[j])
                visited[j] = False
                path.pop()
        dfs(0, target)
        return ans
