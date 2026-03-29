class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        n = len(nums)

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return 
            #选或者不选
            #不选
            dfs(i+1)

            #选
            path.append(nums[i])
            dfs(i+1)
            path.pop()
        dfs(0)
        return ans
            