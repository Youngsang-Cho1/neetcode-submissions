from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for i in tasks:
            d[i] += 1

        d_sorted = sorted(d.items(), key = lambda x:x[1], reverse = True)

        res = 0
        while sum(d.values()):
            for curr in range(n+1):
                if curr < len(d):
                    char = d_sorted[curr][0]
                    if d[char]:
                        d[char] -= 1
                res += 1
                if not sum(d.values()):
                    return res
            d_sorted = sorted(d.items(), key = lambda x:x[1], reverse = True)

            
                





        


        
            

            
