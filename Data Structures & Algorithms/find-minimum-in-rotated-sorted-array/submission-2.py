class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid
            else:
                right = mid
        return nums[right]