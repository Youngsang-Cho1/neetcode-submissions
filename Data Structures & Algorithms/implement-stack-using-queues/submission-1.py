
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        
    def pop(self) -> int:
        second_q = deque()
        for i in range(len(self.q)-1):
            second_q.append(self.q[i])
        stack_top = self.q[-1]
        self.q = second_q
        return stack_top
        
    def top(self) -> int:
        return self.q[-1]
        
    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()