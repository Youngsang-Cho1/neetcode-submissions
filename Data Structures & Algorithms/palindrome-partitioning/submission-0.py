class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                if arr[l] != arr[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        res = []
        path = []

        def backtrack(start):
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start, len(s)):
                if is_palindrome(s[start:end+1]):
                    path.append(s[start:end+1])
                    backtrack(end + 1)
                    path.pop()
        backtrack(0)
        return res
