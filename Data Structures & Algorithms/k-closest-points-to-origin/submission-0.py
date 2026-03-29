class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            #转负数变最大堆
            dist = -(x ** 2 + y ** 2)
            #加入当前距离和坐标
            heapq.heappush(h,[dist, x, y])
            #如果堆里超过 k 个， pop 最大的
            if len(h) > k:
                heapq.heappop(h)
        ans = []
        while len(h) > 0:
            dist, x, y = heapq.heappop(h)
            ans.append([x,y])
        return ans
        