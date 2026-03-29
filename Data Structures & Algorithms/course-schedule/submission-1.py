class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        #set判断之前是否有环
        visiting = set()

        def dfs(course):
            #有环，直接返回 False
            if course in visiting:
                return False
            #没有先修课了，返回True
            if preMap[course] == []:
                return True
            
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            #剪枝，表示所有先修课都没有环
            preMap[course] =  []
            return True
        #从每个点开始，因为图可能不全部相连
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True