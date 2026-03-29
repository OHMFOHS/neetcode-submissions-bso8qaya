class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 #get i th digits
            res += (bit << (31 - i)) #place bit from left to right 31 30 ...... 0
        return res