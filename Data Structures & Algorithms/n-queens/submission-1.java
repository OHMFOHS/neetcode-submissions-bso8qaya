class Solution {
    public List<List<String>> solveNQueens(int n) {
        boolean[] cols = new boolean[n];

        int[] c = new int[n];
        List<List<String>> ans = new ArrayList<>();
        dfs(0, c, n, ans, cols);
        return ans;

    }

    private void dfs(int i, int[] c, int n, List<List<String>> ans, boolean[] cols ) {
        if (i == n) {
            List<String> cur = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                StringBuilder sb = new StringBuilder();
                for(int a = 0; a < c[j]; a++) {
                    sb.append('.');
                }
                sb.append('Q');
                for(int a = 0; a < n - c[j] - 1; a++) {
                    sb.append('.');
                }
                cur.add(sb.toString());
            }
            ans.add(cur);
            return;
        }

        for(int j = 0; j < n; j++) {
            if(!cols[j] && check(i, j, c)) {
                c[i] = j;
                cols[j] = true;
                dfs(i+1, c, n, ans, cols);
                cols[j] = false;
            }
        }
    }

    private boolean check(int r1, int c1, int[] c) {
        for(int i = 0; i < r1; i++) {
            if (r1 + c1 == i + c[i]) return false;
            if(r1 - c1 == i - c[i]) return false;
        } 
        return true;
    }
}
