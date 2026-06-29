class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx, i in enumerate(temperatures):
            idx_diff = 0
            while stack and i > stack[-1][1]:
                stackIdx, stackVal = stack.pop()
                result[stackIdx] = idx - stackIdx
            stack.append([idx, i])
        return result
