class Solution:
    # dict, same str -> left shift to curr
    #       diff str -> right shift by 1
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left = 0
        max_substr = 0
        
        char_set = set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_substr = max(max_substr, right - left + 1)
        return max_substr


        