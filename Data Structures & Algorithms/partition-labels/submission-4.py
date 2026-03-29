class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        #遍历第一遍，记录最后的index
        for i, x in enumerate(s):
            pos[x] = i
        
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            #每次size增加1
            size += 1
            #如果发现比当前end更后面的index，就更新end
            end = max(end, pos[c])
            if i == end:
                res.append(size)
                size = 0
        return res
            

        
