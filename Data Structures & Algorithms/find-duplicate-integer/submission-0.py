class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #detect a cycle

        #intersect first time
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        #Floyd --> intersect for second time
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow 
        