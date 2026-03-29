class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt_s = {}
        cnt_t = {}
        for i in range(len(s)):
            cnt_s[s[i]] = 1 + cnt_s.get(s[i], 0)
            cnt_t[t[i]] = 1 + cnt_t.get(t[i], 0)
        return cnt_s == cnt_t