class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt_s1 = Counter(s1)
        cnt_s2 = defaultdict(int)
        l = len(s1)
        left = 0
        for right in range(len(s2)):
            c = s2[right]
            cnt_s2[c] += 1
            if right - left + 1 > l:
                cnt_s2[s2[left]] -= 1
                if cnt_s2[s2[left]] == 0:
                    del cnt_s2[s2[left]]
                left += 1
            if cnt_s1 == cnt_s2:
                return True
        return False