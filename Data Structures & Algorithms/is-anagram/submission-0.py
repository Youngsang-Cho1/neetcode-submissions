class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = [0] * 26
        str2 = [0] * 26

        for i in s:
            idx = ord(i) - ord('a')
            str1[idx] += 1
        
        for i in t:
            idx = ord(i) - ord('a')
            str2[idx] += 1
        return str1 == str2


            


            




        