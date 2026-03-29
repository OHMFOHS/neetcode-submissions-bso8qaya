class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        n = len(nums)
        def dfs(i, left):
            if left == 0:
                ans.append(path.copy())
                return
            if i == n or left < 0:
                return
            #不选
            dfs(i + 1, left)

            #选
            path.append(nums[i])
            dfs(i, left - nums[i])
            path.pop()
        dfs(0, target)
        return ans