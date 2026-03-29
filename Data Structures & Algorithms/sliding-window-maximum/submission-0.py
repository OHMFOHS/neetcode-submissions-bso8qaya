class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        for i in range(len(nums)):
            #加入堆，转成负数变最大堆
            heapq.heappush(heap, (-nums[i], i))
            # i == k - 1 时窗口形成
            if i >= k - 1:
                #清理堆顶的过期元素，超出滑窗的有效范围
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                #取最大值作为答案
                ans.append(-heap[0][0])
        return ans