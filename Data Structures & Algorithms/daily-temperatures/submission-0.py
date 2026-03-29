class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        # [30, 38, 30, 36]
        # [1]
        ans = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans
