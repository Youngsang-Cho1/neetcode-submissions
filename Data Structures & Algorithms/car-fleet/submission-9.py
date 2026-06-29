class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i, j in zip(position, speed):
            stack.append([i, j])
        stack = sorted(stack, key = lambda x: x[0], reverse = True)
        res = 1

        prev_time = (target - stack[0][0])/stack[0][1]

        for idx in range(1, len(stack)):
            pos, mph = stack[idx]
            curr_time = (target - pos)/mph
            # if the time that the current car takes to get to the target
            # is faster than the front car, group them together
            if curr_time > prev_time:
                res += 1
                prev_time = curr_time
        print(stack)
        return (res)

       