class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        ans = []

        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            #清理过期
            if q[0] < l:
                q.popleft()
            
            if r - l + 1 >= k:
                ans.append(nums[q[0]])
                l += 1
        return ans    
