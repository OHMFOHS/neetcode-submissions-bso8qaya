class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        path = []
        ans = []
        candidates.sort()
        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return
            if i == n or candidates[i] > left:
                return
            for j in range(i, n):
                #确保同一层不重复
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                dfs(j+1, left - candidates[j])
                path.pop()
        dfs(0, target)
        return ans
