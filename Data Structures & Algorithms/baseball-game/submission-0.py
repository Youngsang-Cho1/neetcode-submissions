class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i in '+DC' and stack:
                if i == '+':
                    stack.append(int(stack[-1]) + int(stack[-2]))
                elif i == 'C':
                    stack.pop()
                else:
                    stack.append(int(stack[-1]) * 2)
            else:
                stack.append(int(i))
        print(stack)
        return sum(stack)


        