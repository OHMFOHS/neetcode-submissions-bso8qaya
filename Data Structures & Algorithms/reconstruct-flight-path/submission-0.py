class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src : [] for src, des in tickets}
        #排序保证符合字典序
        tickets.sort()
        for src, des in tickets:
            adj[src].append(des)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            #临时列表，用于这次遍历，避免变遍历边修改
            temp = list(adj[src])
            for i, v in enumerate(temp):
                #pop掉当前票，表示票只能走一次
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i,v)
                res.pop()
            return False
        dfs("JFK")
        return res                