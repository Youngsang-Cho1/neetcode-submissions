class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        s1_val = sum([ord(i) for i in s1])
        print(s1_val)
        s1_len = len(s1)

        for i in range(len(s2)):
            curr = sorted(s2[i:i+s1_len])
            print(curr)
            s2_val = sum([ord(k) for k in curr])
            print(s2_val)
            if s1_val == s2_val and curr == s1_sorted :
                return True
        return False
        
        