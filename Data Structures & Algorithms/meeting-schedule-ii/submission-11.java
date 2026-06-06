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
        //sweep line
        //使用 TreeMap 因为最后遍历需要
        TreeMap<Integer, Integer> cnt = new TreeMap<>();
        for(Interval i : intervals) {
            if (!cnt.containsKey(i.start)) {
                cnt.put(i.start, 1);
            } else {
                cnt.put(i.start, cnt.get(i.start) + 1);
            }
            if (!cnt.containsKey(i.end)) {
                cnt.put(i.end, -1);
            } else {
                cnt.put(i.end, cnt.get(i.end) - 1);
            }
        }
        int ans = 0;
        int rooms = 0;
        for (Map.Entry<Integer, Integer> entry : cnt.entrySet()) {
            rooms += entry.getValue();
            ans = Math.max(ans, rooms);
        }
        return ans;
    }
}
