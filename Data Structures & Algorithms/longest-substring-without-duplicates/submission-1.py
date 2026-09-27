from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_map = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            #print(substr_map)
            substr_map[s[r]] += 1
            while substr_map[s[r]] > 1:
                substr_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


            



        