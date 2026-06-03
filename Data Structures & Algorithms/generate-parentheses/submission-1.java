class Solution {
    public List<String> generateParenthesis(int n) {
        List<Character> path = new ArrayList<>();
        List<String> ans = new ArrayList<>();
        dfs(n, path, ans, 0, 0);
        return ans;

    }

    void dfs(int n, List<Character> path, List<String> ans, int left, int right) {
        if (path.size() == n * 2) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n * 2; i++) {
                sb.append(path.get(i));
            }
            ans.add(sb.toString());
            return;
        }
        
        if(left < n) {
            path.add('(');
            dfs(n, path, ans, left + 1, right);
            path.remove(path.size() - 1);
        }

        if(left > right && right < n) {
            path.add(')');
            dfs(n, path, ans, left, right + 1);
            path.remove(path.size() - 1);
        }
    }
}
