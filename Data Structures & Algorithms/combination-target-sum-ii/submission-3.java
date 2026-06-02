class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        dfs(candidates, target, 0, ans, cur);
        return ans;
    }

    private void dfs(int[] candidates, int target, int i, List<List<Integer>> ans, List<Integer> cur) {
        if(target == 0) {
            ans.add(new ArrayList<>(cur));
            return;
        }

        for(int j = i; j < candidates.length; j++) {
            if (j > i && candidates[j] == candidates[j-1]) continue;
            if (target < candidates[j]) continue;
            target -= candidates[j];
            cur.add(candidates[j]);
            dfs(candidates, target, j + 1, ans, cur);
            target += candidates[j];
            cur.remove(cur.size() - 1);
        }
    }
}
