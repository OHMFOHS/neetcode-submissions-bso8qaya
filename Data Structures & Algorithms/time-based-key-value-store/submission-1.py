class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_store:
            return ""
        values = self.key_store[key]
        left = -1
        right = len(values)
        while left + 1 < right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                left = mid
            else:
                right = mid
        return values[left][0] if left >= 0 else ""
        
