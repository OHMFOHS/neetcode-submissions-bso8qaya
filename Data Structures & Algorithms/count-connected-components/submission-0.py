class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for next_node in adj[node]:
                dfs(next_node)
        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans