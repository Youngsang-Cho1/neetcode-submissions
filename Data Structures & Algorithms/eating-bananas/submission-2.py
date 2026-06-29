class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        if h == len(piles):
            return piles[-1]
        l = 1
        r = piles[-1]
        k = 0
        while l <= r:
            counter = 0
            mid = (l + r) // 2
            print(l, r, mid)
            for i in piles:
                counter += math.ceil(i / mid) 
            if counter > h:
                l = mid + 1
            else:
                k = mid
                r = mid - 1
        return k


            

        

        