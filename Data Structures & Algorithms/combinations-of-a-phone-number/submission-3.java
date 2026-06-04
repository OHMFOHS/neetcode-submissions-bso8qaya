class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0){
            return new ArrayList<>();
        }
        HashMap<Character, String> mp = new HashMap<>();
        mp.put('2', "abc");
        mp.put('3', "def");
        mp.put('4', "ghi");
        mp.put('5', "jkl");
        mp.put('6', "mno");
        mp.put('7', "pqrs");
        mp.put('8', "tuv");
        mp.put('9', "wxyz");

        List<String> ans = new ArrayList<>();
        List<Character> path = new ArrayList<>();
        dfs(mp, ans, path, digits, 0);
        return ans;
    }
    
    private void dfs(HashMap<Character, String> mp, List<String> ans, List<Character> path, String digits, int i) {
        if (i == digits.length()) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < path.size(); j++) {
                sb.append(path.get(j));
            }
            ans.add(sb.toString());
            return;
        }
        String cur = mp.get(digits.charAt(i));
        for(int idx = 0; idx < cur.length(); idx++) {
            path.add(cur.charAt(idx));
            dfs(mp, ans, path, digits, i+1);
            path.remove(path.size() - 1);
        }

    }

}
