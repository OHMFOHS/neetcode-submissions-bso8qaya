class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> cur = new ArrayList<>();
        List<List<Integer>> ans =  new ArrayList<>();
        boolean[] seen = new boolean[nums.length];
        dfs(nums, seen, cur, ans);
        return ans;
    }

    private void dfs(int[] nums, boolean[] seen, List<Integer> cur, List<List<Integer>> ans) {
        if (cur.size() == nums.length) {
            ans.add(new ArrayList<>(cur));
            return;
        }
        for(int i = 0; i < nums.length; i++) {
            if (seen[i]) continue;
            seen[i] = true;
            cur.add(nums[i]);
            dfs(nums, seen, cur, ans);
            cur.remove(cur.size()-1);
            seen[i] = false;
        }
    }
}
