class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #BFS topological sort
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for prerequisite in prerequisites:
                course, pre = prerequisite[0], prerequisite[1]
                adj[pre].append(course)
                indegree[course] += 1
        
        q = deque()
        studied = 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            l = len(q)
            for _ in range(l):
                cur_course = q.popleft()
                studied += 1
                for course in adj[cur_course]:
                    indegree[course] -= 1
                    if indegree[course] == 0:
                        q.append(course)
        return studied == numCourses
        
