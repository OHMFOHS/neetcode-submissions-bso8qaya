class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> mp = new HashMap<>();
        for(String s : strs) {
            int[] cnt = new int[26];
            for(int i = 0; i < s.length(); i++) {
                cnt[s.charAt(i) - 'a']++;
            }

            String key = Arrays.toString(cnt);

            if(mp.containsKey(key)) {
                mp.get(key).add(s);
            }else {
                mp.put(key, new ArrayList<>());
                mp.get(key).add(s);
            }
        }
        List<List<String>> ans = new ArrayList<>();
        for(Map.Entry<String, List<String>> entry: mp.entrySet()) {
            ans.add(entry.getValue());
        }
        return ans;
    };
}
