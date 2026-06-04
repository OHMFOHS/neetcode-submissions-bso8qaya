class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> ans = new ArrayList<>();
        List<String> path = new ArrayList<>();
        dfs(ans, path, 0, s);
        return ans;
    }

    private void dfs(List<List<String>> ans, List<String> path, int i, String s) {
        if (i == s.length()) {
            ans.add(new ArrayList<>(path));
            return;
        }
        for (int j = i + 1; j < s.length() + 1; j++) {
            if(isPalindrome(s.substring(i,j))) {
                path.add(s.substring(i, j));
                dfs(ans, path, j, s);
                path.remove(path.size() - 1);
            }
        }
    }
    private boolean isPalindrome(String s) {
        if(s.length() <=  1) {
            return true;
        }
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if(s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }
}
