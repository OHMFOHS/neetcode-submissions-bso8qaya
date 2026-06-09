class Solution {
    public int[] minInterval(int[][] intervals, int[] queries) {
        //brute force
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int cur = Integer.MAX_VALUE;
            for(int j = 0; j < intervals.length; j++) {
                int start = intervals[j][0];
                int end = intervals[j][1];
                if (queries[i] >= start && queries[i] <= end) {
                    cur = Math.min(cur, end - start + 1);
                }
            }
            if(cur != Integer.MAX_VALUE) {
                ans[i] = cur;
            } else {
                ans[i] = -1;
            }
        }
        return ans;
    }
}
