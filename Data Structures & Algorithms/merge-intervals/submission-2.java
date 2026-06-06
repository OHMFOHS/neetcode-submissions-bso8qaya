class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int[]> ans = new ArrayList<>();
        int n = intervals.length;
        if (n == 1) {
            return intervals;
        }
        ans.add(intervals[0]);
        int i = 1;
        while (i < n) {
            if (intervals[i][0] > ans.get(ans.size() - 1)[1]) {
                ans.add(intervals[i]);                
            } else {
                int[] a = new int[2];
                a[0] = Math.min(intervals[i][0], ans.get(ans.size() - 1)[0]);
                a[1] = Math.max(intervals[i][1], ans.get(ans.size() - 1)[1]);
                ans.remove(ans.size() - 1);
                ans.add(a);
            }
            i++;
        }
        return ans.toArray(new int[ans.size()][]);
    }
}
