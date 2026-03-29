from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        max_f = 0
        ans = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            mp[c] += 1
            max_f = max(max_f, mp[c])
            while right - left + 1 - max_f > k:
                mp[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans