class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sqrt( (x1 - x2)^2 + (y1 - y2)^2 )
        # origin (0, 0), x2 = 0, y2 = 0

        # (x1 - 0)^2 + (y1 - 0)^2
        # x1**2 + y1**2 -> dist

        heap = []

        for x, y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(heap, (dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        print(heap)
        while heap:
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
        
        return res