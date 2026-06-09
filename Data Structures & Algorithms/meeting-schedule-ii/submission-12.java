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
        int ans = 0;
        TreeMap<Integer, Integer> mp = new TreeMap<>();
        for(Interval interval : intervals) {
            mp.put(interval.start, mp.getOrDefault(interval.start, 0) + 1);
            mp.put(interval.end, mp.getOrDefault(interval.end, 0) - 1);
        }
        int rooms = 0;
        for(Map.Entry<Integer, Integer> entry : mp.entrySet()) {
            rooms += entry.getValue();
            ans = Math.max(ans, rooms);
        }
        return ans;
    }
}
