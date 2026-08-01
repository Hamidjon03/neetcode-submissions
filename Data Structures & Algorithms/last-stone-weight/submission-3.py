class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [ 2, 3, 6, 2, 4]  - we need a max heap
        # maxHeap = [6, 4, 3, 2, 2]
        # maxHeap = [3, 3, 2, 2]
        # maxHeap = [2, 2]
        # maxHeap = []
        # return 0
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
            
        stones.append(0)
        return abs(stones[0])