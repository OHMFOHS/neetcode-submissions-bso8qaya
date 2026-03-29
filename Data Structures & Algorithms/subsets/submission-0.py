class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        n = len(nums)
        def dfs(i:int) -> None:
            ans.append(path.copy())
            if i == n:
                return
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return ans
            

        