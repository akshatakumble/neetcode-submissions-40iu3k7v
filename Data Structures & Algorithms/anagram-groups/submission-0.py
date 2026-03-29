class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)  #mapping charCount to list of anagrams
#dictionary that automatically creates an empty list

        for s in strs:
            count = [0]*26 #array for letters a to z

            for c in s:
                count[ord(c) - ord("a")] += 1 #count the occurance of each letter
            
            res[tuple(count)].append(s) #updating new list to with grouped anagrams

        return list(res.values())