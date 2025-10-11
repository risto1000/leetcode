class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['          
        }

        for i in s:
            if i in mapping.values():
                stack.append(i)
            if i in ')]}':
                if not stack:
                    return False
                lastchar = stack.pop()
                if lastchar != mapping[i]:
                    return False
        return not stack
