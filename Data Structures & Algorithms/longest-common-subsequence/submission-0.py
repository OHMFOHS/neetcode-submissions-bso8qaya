class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        #f[i+1][j+1] = max(f[i][j+1], f[i+1][j], f[i][j] + 1) if text1[i] == text1[j]

        f = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    f[i+1][j+1] = max(f[i][j+1], f[i+1][j], f[i][j] + 1)
                else:
                    f[i+1][j+1] = max(f[i][j+1], f[i+1][j], f[i][j])
        return f[-1][-1]