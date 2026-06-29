class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        for i in range(len(heights)):
            print(l,r)
            total = min(heights[l], heights[r]) * (r - l)
            res = max(res, total)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res
            
        # two pointers
        # initialized l, r to 0, 1
        # if r+1 is bigger than r -> r = r+1
        # if l+1 is bigger than l -> l = l+1