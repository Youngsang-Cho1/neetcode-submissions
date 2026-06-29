class Solution:
    def isPalindrome(self, s):
        for idx in range(0, len(s)//2):
            if s[idx] != s[-(idx + 1)]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(len(s)+1):
            for j in range(i, len(s)+1):
                word = s[i:j]
                #print(word)
                if self.isPalindrome(word) and len(word) > len(res):
                    res = word
        return res


        
        