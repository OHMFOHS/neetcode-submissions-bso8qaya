class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for i in range(len(s1)):
            cnt1[ord(s1[i]) - ord('a')] += 1
            cnt2[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            if cnt1[i] == cnt2[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            #add to window
            index = ord(s2[r]) - ord('a')
            cnt2[index] += 1
            if cnt2[index] == cnt1[index]:
                matches += 1
            elif cnt1[index] + 1 == cnt2[index]:
                matches -= 1
            
            #remove from window
            index = ord(s2[l]) - ord('a')
            cnt2[index] -= 1
            if cnt2[index] == cnt1[index]:
                matches += 1
            elif cnt1[index] - 1 == cnt2[index]:
                matches -= 1
            l += 1
        return matches == 26