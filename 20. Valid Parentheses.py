class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        lookup = {")":"(", "}":"{", "]":"["}

        for i in s:
            if i in lookup.values():
                stack.append(i)
            elif stack and lookup[i] == stack[-1]:
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False
        