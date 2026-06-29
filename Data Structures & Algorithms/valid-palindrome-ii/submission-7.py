class Solution:
    def validPalindrome(self, s: str) -> bool:
        is_used = 0
        s_copy = list(s)
        for i in range (len(s)//2):
            if (s[i] != s[-(i+1)]):
                if (not is_used) and (s[i] == s[-(i+2)]):
                    print(s[i], s[-(i+2)])
                    del s_copy[-(i+1)]
                    is_used = 1
                    
                elif (not is_used) and (s[i+1] == s[-(i+1)]):
                    print(s[i+1], s[-(i+1)])
                    del s_copy[i]
                    is_used = 1
        print(s_copy)

        for i in range (len(s_copy)//2):
            if s_copy[i] != s_copy[-(i+1)]:
                return False
        return True
            
        
        