class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        #转换成最大堆
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        #队列存放频率和下一次可执行的时间
        q = deque()
        time = 0
        #当堆或队列不为空时
        while max_heap or q:
            time += 1
            #处理频率最大的任务
            if max_heap:
                freq = 1 + heapq.heappop(max_heap)
                #如果频率不为0， 记录下次可执行时间，加入队列等下次执行
                if freq:
                    q.append([freq, time + n])
            #如果队列第一个到了可执行时间，就加回堆中        
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time