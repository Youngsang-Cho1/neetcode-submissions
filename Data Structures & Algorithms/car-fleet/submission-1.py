class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_map = list(zip(position, speed))
        car_map.sort()

        time = [((target - pos) / sp) for pos, sp in car_map]
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
                

