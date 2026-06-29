class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target 에 도달할때, 몇개의 그룹?
        # position & speed
        stack = []
        for i, j in zip(position, speed):
            stack.append([i, j])
        stack = sorted(stack, key = lambda x: x[0], reverse = True)
        res = len(stack)

        for idx in range(len(stack)):
            pos, mph = stack[idx]
            time = (target - pos)/mph
            if idx != 0:
                prev_time = (target - stack[idx-1][0])/stack[idx-1][1]
                # if the time that the current car takes to get to the target
                # is faster than the front car, group them together
                if time <= prev_time:
                    res -= 1
                    stack[idx] = stack[idx - 1]
        print(stack)
        return (res)

       