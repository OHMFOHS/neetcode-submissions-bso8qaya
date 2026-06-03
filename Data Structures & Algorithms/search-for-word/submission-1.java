class Solution {
    public boolean exist(char[][] board, String word) {
        boolean[][] visited = new boolean[board.length][board[0].length];
        boolean res = false;
        for(int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0)) {
                    res = dfs(board, word, i, j, 0, visited);
                }
                if (res) return true;
            }
        }
        return false;

    }
    private boolean dfs(char[][] board, String word, int x, int y, int i, boolean[][] visited) {
        if (i == word.length()) return true;
        if ( x < 0 || x >= board.length || y < 0 || y >= board[0].length || visited[x][y] || board[x][y] != word.charAt(i)) return false;
        visited[x][y] = true;
        boolean res = false;
        if (dfs(board, word, x-1, y, i + 1, visited) || dfs(board, word, x+1, y, i+1, visited) || dfs(board, word, x, y-1, i+1, visited) || dfs(board, word, x, y+1, i+1, visited) ) {
            res = true;
        }
        visited[x][y] = false;
        return res;
    }
}
