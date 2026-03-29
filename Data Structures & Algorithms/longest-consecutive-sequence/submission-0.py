class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = set(nums)
        ans = 0
        for n in cnt:
            if not n-1 in cnt:
                length = 1
                while n+length in cnt:
                    length +=1
                ans = max(length, ans)
        return ans