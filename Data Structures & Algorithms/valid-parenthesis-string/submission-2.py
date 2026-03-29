class Solution:
    def checkValidString(self, s: str) -> bool:
        #left_min 表示最少的情况（通配符都算 ')' 的情况） 有多少没有匹配的
        #left_max 表示最多的情况（通配符都算 '(' 的情况） 有多少没有匹配的

        left_min, left_max = 0, 0

        for c in s:
            if c == '(':
                left_min += 1 
                left_max += 1
            elif c == ')':  
                left_min -= 1
                left_max -= 1
            else: #meet wildcard 如果是通配符
                left_min -= 1 #算成 ')'
                left_max += 1 #算成 '('
            if left_max < 0: #最多的情况都小于 0， 肯定错
                return False
            if left_min < 0: # 最少的情况小于 0，但是可以弥补所以恢复成 0
                left_min = 0
        return left_min == 0
                

