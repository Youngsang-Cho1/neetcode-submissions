class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_map = [(i,j) for i,j in zip(position, speed)]
        car_map.sort()

        time = [((target - position) / speed) for position, speed in car_map]
        stack = []
        for curr in time:
            if not stack:
                stack.append(curr)
            else:
                if stack[-1] <= curr:
                    while stack and stack[-1] <= curr:
                        stack.pop()
                stack.append(curr)
        return len(stack)
                

