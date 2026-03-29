class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
    def add_string(self, s):
        cur = self
        for c in s:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfString = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #bulid prefix tree
        root = TrieNode()
        for w in words:
            root.add_string(w)
        
        #dfs
        m, n = len(board), len(board[0])
        ans = set()
        def dfs(r, c, node, word):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] == '#' or board[r][c] not in node.children:
                return
            temp = board[r][c]
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfString:
                ans.add(word)
                node.endOfString = False
            board[r][c] = '#'
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            board[r][c] = temp
        for r in range(m):
            for c in range(n):
                dfs(r,c,root,'')
        return list(ans)
