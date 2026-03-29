class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i : [] for i in range(len(points))}
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i,len(points)):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        visited = set()
        cost = 0
        minHeap = [[0,0]]

        while len(visited) < len(points):
            cur_cost, cur_point = heapq.heappop(minHeap)
            if cur_point in visited:
                continue
            visited.add(cur_point)
            cost += cur_cost
            for nei in adj[cur_point]:
                new_cost, new_p = nei
                if new_p not in visited:
                    heapq.heappush(minHeap, [new_cost, new_p])
        return cost