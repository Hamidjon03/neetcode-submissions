class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        for item in matrix:
            n = len(item)
            low = 0
            high = n - 1

            while low <= high:
                middle = low + ((high - low) // 2)

                if target == item[middle]: return True
                if target  > item[middle]: low = middle + 1
                if target  < item[middle]: high = middle - 1

        return False

        