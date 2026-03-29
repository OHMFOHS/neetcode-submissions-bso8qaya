class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        f = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        if len(s1) + len(s2) != len(s3):
            return False
        f[0][0] = True

        for j in range(len(s2)):
            f[0][j+1] = s2[j] == s3[j] and f[0][j]


        for i in range(len(s1)):
            f[i+1][0] = s1[i] == s3[i] and f[i][0]
            for j in range(len(s2)):
                f[i+1][j+1] = (s1[i] == s3[i+j+1] and f[i][j+1]) or (s2[j] == s3[i+j+1] and f[i+1][j])
        return f[-1][-1]