class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem in '+-*/':
                second = int(stack.pop())
                first = int(stack.pop())
                if elem == '+':
                    stack.append(first + second)
                elif elem == '-':
                    stack.append(first - second)
                elif elem == '*':
                    stack.append(first * second)
                elif elem == '/':
                    stack.append(int(first / second))
            else:
                stack.append(int(elem))
        return stack[-1]