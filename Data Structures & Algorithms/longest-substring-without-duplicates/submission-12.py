from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1
        d = defaultdict(int)
        l, r = 0, 1
        d[s[l]] += 1

        while r < len(s):
            if d[s[r]] == 0:
                d[s[r]] += 1
                r += 1
                
            elif d[s[r]] == 1:
                
                curr = r - l # r not included yet
                #print(l, r, curr)
                res = max(res, curr)
                d[s[l]] -= 1
                l += 1

            #print(d)
        return max(res, r - l)

                

'''bacdafg
bacd, a -> cdafg -> curr = 5
        '''

        