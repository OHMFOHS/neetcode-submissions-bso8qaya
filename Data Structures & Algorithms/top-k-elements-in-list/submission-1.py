class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #bucket sort
        cnt = Counter(nums)
        max_length = max(cnt.values())
        #注意这里为了匹配上次数要+1, 比如最多五次放index 5, 需要长度为 6
        buckets = [[] for _ in range(max_length + 1)]
        for num, freq in cnt.items():
            buckets[freq].append(num)
        res = []
        # for bucket in reversed(buckets):
        #     for num in bucket:
        #         res.append(num)
        #         if len(res) == k:
        #             return res
        #如果不用 reversed()
        for i in range(len(buckets) - 1 , 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res    
