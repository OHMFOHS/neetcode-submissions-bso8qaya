class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        nums.sort()
        def dfs(i):
            ans.append(path.copy())
            if i == n:
                return
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return ans