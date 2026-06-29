class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hashmap = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
       
        for i in s1:
            s1_hashmap[i] += 1
        
        for j in range(len(s2) - len(s1) + 1):
            s2_hashmap = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}

            for k in range(j, len(s1)+j):
                s2_hashmap[s2[k]] += 1
            
            counter = 0
            for i in ('abcdefghijklmnopqrstuvwxyz'):
                if s2_hashmap[i] == s1_hashmap[i]:
                    counter += 1
            if counter == 26:
                return True
        return False
            


        