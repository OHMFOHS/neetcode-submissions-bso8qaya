class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt_s = defaultdict(int)
        cnt_t = defaultdict(int)
        for i in range(len(s)):
            cnt_s[s[i]] += 1
            cnt_t[t[i]] += 1
        return cnt_s == cnt_t