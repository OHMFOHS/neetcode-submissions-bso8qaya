class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_size = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_size = max(max_size, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            max_size = max(max_size, (len(heights) - i) * h)
        return max_size