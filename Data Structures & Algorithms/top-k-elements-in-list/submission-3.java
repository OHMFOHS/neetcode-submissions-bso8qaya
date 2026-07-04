class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> cnt = new HashMap<>();
        for(int n : nums) {
            cnt.put(n, cnt.getOrDefault(n, 0) + 1);
        }

        List<List<Integer>> freq = new ArrayList<>();
        for(int i = 0; i < nums.length + 1; i++) {
            freq.add(new ArrayList<>());
        }
        
        for(Map.Entry<Integer, Integer> entry : cnt.entrySet()) {
            freq.get(entry.getValue()).add(entry.getKey());
        }

        int[] ans = new int[k];
        int idx = 0;
        for(int i = freq.size() - 1; i >= 0; i--) {
            for(int j = 0; j < freq.get(i).size(); j++) {
                ans[idx] = freq.get(i).get(j);
                idx++;
                if(idx == k) return ans;           
            }
        }
        return ans;
    }
}
