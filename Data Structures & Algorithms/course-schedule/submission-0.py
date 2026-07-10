from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. O'zgaruvchilarni tayyorlash
        indegree = [0] * numCourses
        adj = defaultdict(list)

        # 2. Grafni qurish va indegree'larni hisoblash
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1

        # 3. Navbatni tayyorlash (sharti yo'q darslarni qo'shish)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # 4. Asosiy BFS sikli (Kahn algoritmi)
        complete_courses = 0

        while q:
            node = q.popleft()
            complete_courses += 1
            
            # Joriy darsga bog'liq keyingi darslarni aylanib chiqamiz
            for next_course in adj[node]:
                indegree[next_course] -= 1
                
                # Agar shartlar tugasa (0 bo'lsa), o'qish mumkin
                if indegree[next_course] == 0:
                    q.append(next_course)
        
        # 5. Yakuniy tekshiruv: barcha darslar o'qildimi?
        return complete_courses == numCourses