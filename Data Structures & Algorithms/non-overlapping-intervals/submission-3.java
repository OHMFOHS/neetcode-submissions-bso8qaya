class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> a[0] - b[0]);
        return intervals.length - dfs(0, -1, intervals);
    }

    private int dfs(int i, int prev, int[][] intervals) {
        if (i == intervals.length) {
            return 0;
        }
        //不选
        int res = dfs(i + 1, prev, intervals);
        //选
        if (intervals[i][0] >= prev || prev == -1) {
            res = Math.max(res, 1 + dfs(i + 1, intervals[i][1], intervals));
        }
        return res;
    }
}
