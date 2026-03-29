class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #empty string
        for s in strs:
            res += str(len(s)) + "#" + s  # 4#neet
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # what position of the input we're at in the input string so far
        
        while i < len(s):
            j = i #finding end of integer and beginning of delimiter
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #len of s from int to #
            res.append(s[j+1 : j+1+length])
            i = j+1+length
        
        return res