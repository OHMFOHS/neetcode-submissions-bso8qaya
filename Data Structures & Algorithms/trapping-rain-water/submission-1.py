class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        prefix = height[left]
        postfix = height[right]
        ans = 0
        while left <= right:
            if prefix < postfix:
                ans += prefix - height[left]
                left += 1
                prefix = max(prefix, height[left])
            else:
                ans += postfix - height[right]
                right -= 1
                postfix = max(postfix, height[right])
        return ans
