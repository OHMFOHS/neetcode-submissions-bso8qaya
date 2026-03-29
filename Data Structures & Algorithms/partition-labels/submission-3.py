class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        for i, x in enumerate(s):
            pos[x] = i
        
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            
            end = max(end, pos[c])

            if i == end:
                res.append(size)
                size = 0
        return res
            

        
