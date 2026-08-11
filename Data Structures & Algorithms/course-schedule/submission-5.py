class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            
        while q:
            crs = q.popleft()
            numCourses -= 1

            for nei in adj[crs]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return numCourses == 0