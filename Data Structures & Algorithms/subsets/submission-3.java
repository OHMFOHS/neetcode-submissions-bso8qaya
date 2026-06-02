class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        int n = nums.length;
        dfs(nums, 0, ans, cur);
        return ans;

    }
    private void dfs(int[] nums, int start, List<List<Integer>> ans, List<Integer> cur) {
        if (start == nums.length) {
            ans.add(new ArrayList<>(cur));
            return;
        }

        cur.add(nums[start]);
        dfs(nums, start + 1, ans, cur);
        cur.remove(cur.size() - 1);

        dfs(nums, start + 1, ans, cur);

    }
}
