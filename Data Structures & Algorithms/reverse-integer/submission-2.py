class Solution:
    def reverse(self, x: int) -> int:
        MIN = - 2 ** 31
        MAX = 2 ** 31 - 1

        res = 0

        while x:
            #防止python负数取余出错
            digit = int(math.fmod(x,10))
            x = int(x / 10) #float 除法再转int 保证可以向0 取整
            #我们要提前判断下一步会不会导致越界
            #首先比较如果现在的res 已经比 MAX // 10大，那么下一个 digit 加什么都会越界
            #或者当前res 已经和MAX // 10（也就是 MAX 除了最后一位一样）， 然后最后一位也更大，那就超出
            #直接返回0
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit
        return res