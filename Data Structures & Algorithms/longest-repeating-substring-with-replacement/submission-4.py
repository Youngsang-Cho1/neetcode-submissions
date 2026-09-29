class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_len = 0
        charSet = set(s)
        used = 0
        
        for ch in charSet:
            used = 0
            l = 0
            for r in range(len(s)):
                if ch != s[r]:
                    used += 1

                while used > k:
                    if s[l] != ch:
                        used -= 1
                    l += 1

                max_len = max(max_len, r - l + 1)
            
        return max_len