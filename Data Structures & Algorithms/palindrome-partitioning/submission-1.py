class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                if arr[l] != arr[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(idx, path, curr):
            if idx == len(s):
                if not curr:
                    res.append((path.copy()))
                return
            curr += s[idx]
            if is_palindrome(curr):
                path.append(curr)
                backtrack(idx+1, path, '')
                path.pop()
                backtrack(idx+1, path, curr)
            else:
                backtrack(idx+1, path, curr)
        
        backtrack(0, [], '')
        return res
