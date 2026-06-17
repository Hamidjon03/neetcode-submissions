class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum rate k
        # eat all in h hours

        # min_speed = 1 | max_speed = max(piles)
        # check for speed

        low = 1
        high = max(piles)

        while low <= high:
            mid_speed = low + ((high - low) // 2)
            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid_speed - 1) // mid_speed # ceil
            
            if total_hours > h:
                low = mid_speed + 1
            if total_hours <= h:
                high = mid_speed - 1
        
        return low