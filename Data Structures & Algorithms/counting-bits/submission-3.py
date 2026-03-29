class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            cnt = 0
            for i in range(32):
                if num & (1 << i):
                    cnt += 1
            ans.append(cnt)
        return ans