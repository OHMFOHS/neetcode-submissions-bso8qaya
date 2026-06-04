class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> ans = new ArrayList<>();
        List<String> path = new ArrayList<>();
        dfs(ans, path, 0, s);
        return ans;
 
    }
    //枚举可能结束的下标
    private void dfs(List<List<String>> ans, List<String> path, int i, String s) {
        if (i == s.length()) {
            ans.add(new ArrayList<>(path));
            return;
        }
        for (int j = i + 1; j < s.length() + 1; j++) {
            if (isPalindrome(s.substring(i, j))) {
                path.add(s.substring(i, j));
                dfs(ans, path, j, s);
                path.remove(path.size() - 1);
            }
        }

    }


    private boolean isPalindrome(String s) {
        if (s.length() <= 1) return true;
        int start = 0;
        int end = s.length() - 1;

        while(start < end) {
            if (s.charAt(start) != s.charAt(end)) {
                return false;
            }
            start += 1;
            end -= 1;
        }
        return true;
    }
}
