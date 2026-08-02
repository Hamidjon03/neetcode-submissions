class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        # [2,3,6,2,4]
        # [-6, -4, -3, -2, -2]
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        print(stones)
            
        return abs(stones[0]) if stones else 0