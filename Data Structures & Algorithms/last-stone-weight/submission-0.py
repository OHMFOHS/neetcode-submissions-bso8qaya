class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            num1 = -heapq.heappop(stones)
            num2 = -heapq.heappop(stones)
            if num1 > num2:
                heapq.heappush(stones, -(num1-num2))
        return abs(stones[0]) if len(stones) == 1 else 0