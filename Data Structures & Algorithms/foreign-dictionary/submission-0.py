class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #使用set，便于处理重复的字符顺序
        #a = {b, c} 就表示 a 在 b 和 c 前面
        adj = {c : set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            #短的前缀排在更长的词语后面,肯定不对
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []

        def dfs(c):
            #如果访问过，在path就返回True表示有环
            if c in visited:
                return visited[c]
            
            visited[c] = True
            for neiChar in adj[c]:
                if dfs(neiChar):
                    return True
            visited[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return ''.join(res)
