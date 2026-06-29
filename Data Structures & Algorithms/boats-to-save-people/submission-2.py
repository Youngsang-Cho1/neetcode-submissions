class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        l = 0
        r = len(people) - 1

        people.sort()
        # 1 2 2 3 3
        while l <= r:
            remainder = limit - people[r]
            if people[l] <= remainder:
                l += 1
            res += 1
            r -= 1
        return res
        

            

            
            

        