class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp = [0] * (n + 1)
        # offset = 1
        # for i in range(1, n + 1):
        #     if offset * 2 == i:
        #         offset = i
        #     dp[i] = 1 + dp[i-offset]
        # return dp
        ans = []
        cnt = 0
        for i in range(n + 1):
            cnt = 0
            for j in range(32):
                if i & (1 << j):
                    cnt += 1
            ans.append(cnt)
        return ans

                
