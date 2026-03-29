class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,n in enumerate(nums): # enumerate allows key i: value n pairs
            diff = target - n

            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] =  i   #updating hashmap     