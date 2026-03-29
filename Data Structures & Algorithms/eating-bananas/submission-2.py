class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_valid(piles, k, h):
            hour_need = 0
            for banana in piles:
                hour_need += banana // k
                if banana % k:
                    hour_need += 1
            return hour_need <= h
        left = 0
        right = max(piles)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if is_valid(piles, mid, h):
                right = mid
            else:
                left = mid
        return right
