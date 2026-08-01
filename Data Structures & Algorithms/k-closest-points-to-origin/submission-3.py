class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sqrt( (x1 - x2)^2 + (y1 - y2)^2 )
        # x1-x2 + y1 + y2
        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)


        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)

            res.append([x, y])
        
        return res
