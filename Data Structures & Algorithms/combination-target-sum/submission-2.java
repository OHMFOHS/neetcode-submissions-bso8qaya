class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<Integer> cur = new ArrayList<>();
        List<List<Integer>> ans = new ArrayList<>();
        dfs(nums, target, 0, cur, ans);
        return ans;


    }
    private void dfs(int[] nums, int target, int i, List<Integer> cur, List<List<Integer>> ans) {
        if (target < 0 || i == nums.length) return;
        if (target == 0) {
            ans.add(new ArrayList<>(cur));
            return;
        }
        
        target -= nums[i];
        cur.add(nums[i]);
        dfs(nums, target, i, cur, ans);
        target += nums[i];
        cur.remove(cur.size() - 1);

        dfs(nums, target, i+1, cur, ans);
    }
}
