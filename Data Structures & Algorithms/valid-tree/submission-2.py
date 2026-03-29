class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        visited = set()

        def dfs(cur, prev):
            if cur in visited:
                return False
            visited.add(cur)
            for next_node in g[cur]:
                if next_node == prev:
                    continue
                if not dfs(next_node, cur):
                    return False 
            return True

        res = dfs(0, -1)
        return res and len(visited) == n