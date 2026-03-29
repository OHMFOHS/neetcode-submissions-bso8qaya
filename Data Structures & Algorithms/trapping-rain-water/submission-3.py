class Solution:
    def trap(self, height: List[int]) -> int:
        #monotic stack
        st = []
        ans = 0
        for i, h in enumerate(height):
            while st and h >= height[st[-1]]:
                bottom_h = height[st.pop()]
                if not st:
                    break
                left = st[-1]
                dh = min(height[left], h) - bottom_h
                ans += dh * (i - left - 1)
            st.append(i)
        return ans
            