class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #bucket sort
        cnt = Counter(nums)
        max_length = max(cnt.values())

        buckets = [[] for _ in range(max_length + 1)]
        for num, freq in cnt.items():
            buckets[freq].append(num)
        res = []
        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
            
