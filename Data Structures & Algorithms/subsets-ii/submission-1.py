class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            #basecase - if its end of list return res
            if i == len(nums):
                res.append(subset[::]) #make copy of subset
                return

            #All subsets that should be included in nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            #all subsets not to be included
            while i+1 < len(nums) and nums[i] == nums[i+1]: #skip duplicates
                i+=1
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return res