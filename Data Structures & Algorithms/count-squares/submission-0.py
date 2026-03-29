class CountSquares:

    def __init__(self):
        self.points_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points_count[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        for p in list(self.points_count.keys()):
            cnt = self.points_count[p]
            if abs(p[0] - point[0]) == abs(p[1] - point[1]) and p[0] != point[0] and p[1] != point[1]:
                res += cnt * self.points_count[(point[0], p[1])] * self.points_count[(p[0], point[1])]
        return res
        
