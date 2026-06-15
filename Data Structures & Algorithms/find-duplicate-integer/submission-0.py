class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # first approach will be using sort and compare items
        # count frequency of itmes
        # fast and slow pointer

        fast = 0
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
    
        return slow
        