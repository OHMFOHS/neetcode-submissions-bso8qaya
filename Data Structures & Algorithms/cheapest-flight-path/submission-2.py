class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        #建表
        adj = [[] for _ in range(n)]
        #从 src 出发， 用了 i 条边，需要的最小花费
        dist = [[INF] * (k + 5) for _ in range(n)]
        for u, v, cost in flights:
            #u 已经是数字代表的城市，所以可以直接 adj[u]建表
            adj[u].append([v,cost])
        
        dist[src][0] = 0
        #src加入堆
        minHeap = [(0, src, -1)] #cost, node, stops

        while len(minHeap):
            cost, node, stops = heapq.heappop(minHeap)
            if dst == node: return cost
            #如果中转次数用完 或者 状态不是最优
            if stops == k or dist[node][stops + 1] < cost:
                continue
            for nei, w in adj[node]:
                nextCost = cost + w
                nextStops = stops + 1
                if dist[nei][nextStops + 1] > nextCost:
                    dist[nei][nextStops + 1] = nextCost
                    heapq.heappush(minHeap, (nextCost, nei, nextStops))
        return -1
