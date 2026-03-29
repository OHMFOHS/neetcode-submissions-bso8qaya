class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if not i in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if minH[0] != i:
                        return False
                    heapq.heappop(minH)
        return True

