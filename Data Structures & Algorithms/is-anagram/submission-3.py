class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict={}
        for char in s:
            if char not in anagram_dict.keys():
                anagram_dict[char] = 1
            else:
                anagram_dict[char] += 1

        for char in t:
            if char in anagram_dict.keys() and anagram_dict[char] > 0:
                anagram_dict[char] -= 1
            else:
                return False
        print(anagram_dict)
        if sum(anagram_dict.values()) != 0:
            return False
    
        return True
            


            




        