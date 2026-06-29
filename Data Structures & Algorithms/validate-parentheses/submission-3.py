class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_brackets = ['()', '[]', '{}']
        idx = 0
        while idx != len(s):
            stack.append(s[idx])
            print(stack)
            if (len(stack) >= 2) and (stack[-2] + stack[-1] in valid_brackets):
                stack.pop()
                stack.pop()
            idx += 1
        print(stack)
        if stack:
            return False
        return True
        
        