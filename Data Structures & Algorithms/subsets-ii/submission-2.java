class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<Integer> path = new ArrayList<>();
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);
        dfs(0, nums, path, ans);
        return ans;
    }

    private void dfs(int i, int[]nums, List<Integer> path, List<List<Integer>> ans) {
        ans.add(new ArrayList<>(path));
        for(int j = i; j < nums.length; j++) {
            if (j > i && nums[j] == nums[j-1]) continue;
            path.add(nums[j]);
            dfs(j  + 1, nums, path, ans);
            path.remove(path.size()-1);
        }
    }
}
