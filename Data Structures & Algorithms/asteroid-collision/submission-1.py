class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in (asteroids):
            while stack and i < 0 and stack[-1] > 0:
                curr = i
                last = stack[-1]
                if abs(curr) > abs(last):
                    stack.pop()
                elif abs(curr) == abs(last):
                    stack.pop()
                    i = 0
                else:
                    i = 0
            if i:
                stack.append(i)
        return stack
            
            


            
            
        