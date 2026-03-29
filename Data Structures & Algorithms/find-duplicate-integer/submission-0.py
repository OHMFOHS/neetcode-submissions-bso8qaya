class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                p = 0
                while p != slow:
                    p = nums[p]
                    slow = nums[slow]
                return p