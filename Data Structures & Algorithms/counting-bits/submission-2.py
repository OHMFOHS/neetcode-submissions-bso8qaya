class Solution:
    def countBits(self, n: int) -> List[int]:
        #brute force
        ans = []
        cnt = 0
        for num in range(n + 1):
            cnt = 0
            for i in range(32):
                # cnt += num & (1 << i)
                if num & (1 << i):
                    cnt += 1
            ans.append(cnt)
        return ans