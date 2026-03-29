class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        f = [False] * (len(s2) + 1)
        #注意判断边界条件，不相等的情况直接返回 False
        if len(s1) + len(s2) != len(s3):
            return False
        f[0] = True

        for j in range(len(s2)):
            f[j+1] = s2[j] == s3[j] and f[j]
        
        for i in range(len(s1)):
            f[0] = s1[i] == s3[i] and f[0]
            for j in range(len(s2)):
                f[j+1] = (s1[i] == s3[i+j+1] and f[j+1]) or (s2[j] == s3[i+j+1] and f[j])
        return f[-1]