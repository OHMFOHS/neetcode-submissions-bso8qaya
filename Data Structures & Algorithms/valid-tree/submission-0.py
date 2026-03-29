class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if not n:
            return True
        
        adj = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for next_node in adj[node]:
                if next_node == prev:
                    continue
                if not dfs(next_node, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
