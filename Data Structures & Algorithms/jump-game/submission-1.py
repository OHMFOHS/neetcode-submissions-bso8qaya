
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            #如果这个点能到 goal，就把 goal 移动到这个点
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False