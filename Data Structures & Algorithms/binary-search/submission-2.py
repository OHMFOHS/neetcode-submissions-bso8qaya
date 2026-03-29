class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = right + (left - right) // 2
            #严格维护
            #nums[left] < target
            #nums[right] >= target
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        return right if right != len(nums) and nums[right] == target else -1


    