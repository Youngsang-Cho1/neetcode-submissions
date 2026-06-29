class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        l = 0

        people.sort()
        # 1 2 2 3 3

        while people:
            r = len(people) - 1
            if r == 0:
                res += 1
                people.pop(r)
            elif people[l] + people[r] <= limit:
                res += 1
                people.pop(r)
                people.pop(l)
            else:
                res += 1
                people.pop(r)
   
        return res


            

            
            

        