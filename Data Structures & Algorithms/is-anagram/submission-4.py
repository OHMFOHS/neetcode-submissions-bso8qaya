class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] += 1
            cnt[ord(t[i]) - ord('a')] -= 1
        for num in cnt:
            if num > 0:
                return False
        return True