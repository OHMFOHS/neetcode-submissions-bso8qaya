class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.selfsquare(n)
        
        while slow != fast:
            fast = self.selfsquare(fast)
            fast = self.selfsquare(fast)
            slow = self.selfsquare(slow)
        return fast == 1
    
    #返回逐位平方和
    #log(n) time
    def selfsquare(self, n):
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n //= 10
        return sum