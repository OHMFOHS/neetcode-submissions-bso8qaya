class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # f[i+1][j+1] = f[i][j] + 1 (s[i] == t[j])
        #              max (f[i][j+1] , f[i+1][j])
        f = [0] * (len(text2) + 1)
        for i in range(len(text1)):
            prev = f[0]
            for j in range(len(text2)):
                temp = f[j+1]
                if text1[i] == text2[j]:
                    f[j+1] = prev + 1
                else:
                    f[j+1] = max(f[j+1], f[j])
                prev = temp
        return f[len(text2)]