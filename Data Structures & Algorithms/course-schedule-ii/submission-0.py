class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)
            indegree[course] += 1

        result = []
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        
        while q:
            node = q.popleft()
            result.append(node)
            numCourses -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if numCourses != 0:
            return []
        
        return result