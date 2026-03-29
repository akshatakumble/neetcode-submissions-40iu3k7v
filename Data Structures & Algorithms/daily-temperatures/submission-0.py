class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures): #enumerate gives you value and 
            while stack and t>stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = (i-stackIndex)
            stack.append([t,i])
        return res

        