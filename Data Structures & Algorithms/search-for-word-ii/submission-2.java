class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        List<String> ans = new ArrayList<>();
        int m = board.length;
        int n = board[0].length;
        for(String s : words) {
            boolean found = false;
            for(int i = 0; i < m && found == false; i++) {
                for(int j = 0; j < n && found == false; j++) {
                    if (board[i][j] == s.charAt(0)) {
                        if(dfs(i, j, 0, s, board)) {
                            ans.add(s);
                            found = true;
                        }
                    }
                }
            }
        }
        return ans;
    }
    //注意一定要有， 寻找完之后， 标记为已经访问
    private boolean dfs(int x, int y, int i, String target, char[][] board) {
        if (i == target.length()) {
            return true;
        }
        if(x < 0 || y < 0 || x >= board.length || y >= board[0].length || board[x][y] != target.charAt(i) ) {
            return false;
        }
        char tmp = board[x][y];
        board[x][y] = '#';
        boolean res = dfs(x-1, y, i+1, target, board) || dfs(x+1, y, i+1, target, board) || dfs(x, y+1, i+1, target, board) || dfs(x, y-1, i+1, target, board);
        board[x][y] = tmp;
        return res;
    }
}
