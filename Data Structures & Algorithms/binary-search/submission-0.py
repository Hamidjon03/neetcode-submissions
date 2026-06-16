class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                low = middle + 1
            if nums[middle] > target:
                high = middle - 1

        return -1