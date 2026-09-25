class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = []
        for i in s:
            if i.isalnum():
                filtered_s.append(i)
        filtered_s = ''.join(filtered_s).lower()

        print(filtered_s)
        l, r = 0, len(filtered_s) - 1
        while l <= r:
            if filtered_s[l] != filtered_s[r]:
                return False
            l += 1
            r -= 1
        return True

        