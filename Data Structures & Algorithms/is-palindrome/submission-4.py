class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_trimmed = ''
        for i in s:
            char = i.lower()
            if char.isalnum():
                s_trimmed += char
    

        for i in range (0, len(s_trimmed)//2):
            print((s_trimmed[i], s_trimmed[-(i+1)]))
            if s_trimmed[i] != s_trimmed[-(i+1)]:
                return False
        return True

        