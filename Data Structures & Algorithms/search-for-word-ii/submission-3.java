class TrieNode {
    TrieNode[] children;
    int idx;
    TrieNode() {
        children = new TrieNode[26];
        idx = -1;
    }
}

class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        //build Trie First
        TrieNode root = new TrieNode();
        for(int id = 0; id < words.length; id++){
            String s = words[id];
            TrieNode cur = root;
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                int index = c - 'a';
                if(cur.children[index] == null) {
                    cur.children[index] = new TrieNode();
                }
                cur = cur.children[index];
            }
            cur.idx = id;
        }

        List<String> ans = new ArrayList<>();
        for(int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                dfs(i,j,root,board,ans,words);
            }
        }
        return ans;


    }

    private void dfs(int x, int y, TrieNode cur, char[][] board, List<String> ans, String[] words) {
        if (x < 0 || y < 0 || x >= board.length || y >= board[0].length || board[x][y] == '#') {
            return;
        }
        char ch = board[x][y];
        if(cur.children[ch - 'a'] == null) {
            return;
        }
        TrieNode next = cur.children[ch - 'a'];
        if (next.idx != -1) {
            ans.add(words[next.idx]);
            next.idx = -1;
        }
        char tmp = board[x][y];
        board[x][y] = '#';
        dfs(x-1,y,next,board,ans,words);
        dfs(x+1,y,next,board,ans,words);
        dfs(x,y-1,next,board,ans,words);
        dfs(x,y+1,next,board,ans,words);
        board[x][y] = tmp;
    }

}
