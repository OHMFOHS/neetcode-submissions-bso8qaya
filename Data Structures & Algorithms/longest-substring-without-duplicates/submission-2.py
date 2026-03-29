class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mp:
                #如果发现重复，直接跳到最后一次出现的index+1或者l 较大的一个
                l = max(mp[s[r]] + 1, l)
            #记录当前字符的最后位置为r
            mp[s[r]] = r
            res = max(res, r-l+1)
        return res