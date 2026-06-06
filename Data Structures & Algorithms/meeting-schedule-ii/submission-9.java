/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        intervals.sort((a,b) -> a.start - b.start);
        PriorityQueue<Integer> min_heap = new PriorityQueue<>();
        for(Interval interval : intervals) {
            if(!min_heap.isEmpty() && interval.start < min_heap.peek()) {
                min_heap.offer(interval.end);
            } else {
                if (min_heap.isEmpty()) {
                    min_heap.offer(interval.end);
                } else {
                    min_heap.poll();
                    min_heap.offer(interval.end);
                }
            }
        }
        return min_heap.size();
    }
}
