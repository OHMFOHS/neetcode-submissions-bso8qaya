class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        cnt_t = Counter(t)
        window = Counter()

        have, need = 0, len(cnt_t)
        ans_l, ans_r = float("-inf"), float("inf")
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            
            if c in cnt_t and window[c] == cnt_t[c]:
                have += 1
            
            while have == need:
                if r - l < ans_r - ans_l:
                    ans_r, ans_l = r, l

                window[s[l]] -= 1
                if s[l] in cnt_t and window[s[l]] + 1 == cnt_t[s[l]]:
                    have -= 1
                l += 1
        return s[ans_l : ans_r + 1] if ans_l != float("-inf") else ""