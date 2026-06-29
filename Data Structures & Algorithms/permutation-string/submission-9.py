class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        s1_len = len(s1)

        for i in range(len(s2)):
            curr = sorted(s2[i:i+s1_len])
            if curr == s1_sorted :
                return True
        return False
        
        