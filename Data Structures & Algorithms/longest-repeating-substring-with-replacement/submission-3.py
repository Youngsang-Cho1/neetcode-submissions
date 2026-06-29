class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        max_c = 0
        for r in range(len(s)):
            if s[r] in count.keys():
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            max_c = max(max_c, count[s[r]])
                # total length
            while (r - l + 1) - max_c > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res



        
