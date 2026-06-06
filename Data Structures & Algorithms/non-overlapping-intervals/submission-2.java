class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int ans = 0;
        Arrays.sort(intervals, (a,b) -> a[0] - b[0]);
        int end = Integer.MIN_VALUE;
        for(int[] interval : intervals) {
            if (interval[0] < end) {
                end = Math.min(end, interval[1]);
                ans += 1;
            } else {
                end = interval[1];
            }
        }
        return ans;
    }
}
