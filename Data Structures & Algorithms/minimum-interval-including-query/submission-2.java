class Solution {
    public int[] minInterval(int[][] intervals, int[] queries) {
        int m = intervals.length;
        int n = queries.length;
        Arrays.sort(intervals, (a,b) -> a[0] - b[0]);
        //queries 排序并且保留原始下标
        int[][] q = new int[n][2];
        for(int i = 0; i < n; i++) {
            q[i][0] = queries[i];
            q[i][1] = i;
        }
        Arrays.sort(q, (a,b) -> a[0] - b[0]);

        int[] ans = new int[n];
        Arrays.fill(ans, -1);

        //建堆
        //[length, end]
        PriorityQueue<int[]> heap = new PriorityQueue<>((a,b) -> {
            if(a[0] != b[0]) {
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });
        int i = 0;
        for (int[] combinedQuery : q) {
            int query = combinedQuery[0];
            int originalIdx = combinedQuery[1];

            //以长度为顺序， 加入所有比当前 query 小的开始的 interval
            while(i < m && intervals[i][0] <= query) {
                int l = intervals[i][0];
                int r = intervals[i][1];
                int len = r - l + 1;
                heap.offer(new int[]{len, r});
                i++;
            }
            //弹出所有 end < query 的
            while(!heap.isEmpty() && heap.peek()[1] < query) {
                heap.poll();
            }
            if (!heap.isEmpty()) {
                ans[originalIdx] = heap.peek()[0];
            }
        }
        return ans;
    }
}
