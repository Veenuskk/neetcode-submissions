class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for i in operations :
            if i == "+" :
                res = res + int(stack[-1] + stack[-2])
                stack.append(stack[-1] + stack[-2])
            elif i == "D" :
                res = res + int(2 * stack[-1])
                stack.append( 2 * stack[-1])
            elif i == "C" :
                res = res - int(stack[-1])
                stack.pop()
            else :
                res = res + int(i)
                stack.append(int(i))
        return res