from collections import defaultdict
import heapq
from typing import List


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Adjacency list hosil qilamiz
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # 2. Min-Heap: (vaqt, tugun)
        pq = [(0, k)]

        # Eng qisqa vaqtlarni saqlash uchun lug'at
        dist = {}

        while pq:
            time, node = heapq.heappop(pq)

            # Agar bu tugunga avval kelgan bo'lsak, o'tkazib yuboramiz
            if node in dist:
                continue

            dist[node] = time

            # Barcha qo'shnilarga signal yuboramiz
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (time + weight, neighbor))

        # 3. Agar barcha n ta tugunga yetib borgan bo'lsak
        if len(dist) == n:
            return max(dist.values())

        return -1