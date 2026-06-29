class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm_dict = {}
        for char in s1:
            if char not in perm_dict.keys():
                perm_dict[char] = 1
            else:
                perm_dict[char] += 1
        print(perm_dict)
        
        idx = 0
        while idx < len(s2):
            substr_dict = {}
            if s2[idx] in perm_dict:
                counter = 0
                while counter < len(s1) and idx + counter < len(s2):
                    char = s2[idx + counter]
                    if char not in substr_dict:
                        substr_dict[char] = 1
                    else:
                        substr_dict[char] += 1
                    counter += 1
            if substr_dict == perm_dict:
                return True
            idx += 1
        return False
        