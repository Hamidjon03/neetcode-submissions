class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            rem = total % k
            
            if rem in remainder:
                if i - remainder[rem] > 1:
                    return True
                continue
            
            remainder[rem] = i

        return False