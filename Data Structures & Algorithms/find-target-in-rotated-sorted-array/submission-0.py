class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            x = nums[mid]
            if x <= nums[-1] < target:#x 在第二段，target在第一段
                right = mid
            elif target <= nums[-1] < x: #x在第一段，target 在第二段
                left = mid
            elif x >= target:
                right = mid
            else:
                left = mid
        return right if right < len(nums) and nums[right] == target else -1

        