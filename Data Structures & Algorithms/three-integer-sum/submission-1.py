class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(0, n - 2):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                sum = x + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                elif sum == 0:
                    ans.append([x, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
        return ans