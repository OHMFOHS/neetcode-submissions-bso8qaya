class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for info in prerequisites:
            course, pre = info[0], info[1]
            adj[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            l = len(q)
            for _ in range(l):
                cur_course = q.popleft()
                ans.append(cur_course)
                for course in adj[cur_course]:
                    indegree[course] -= 1
                    if indegree[course] == 0:
                        q.append(course)
        return ans if len(ans) == numCourses else []

