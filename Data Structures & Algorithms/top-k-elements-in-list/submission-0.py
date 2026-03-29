class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

#bubble sort 
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
#finding top k
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: #checking list of lists
                res.append(n)
                if len(res) == k: #top k
                    return res
