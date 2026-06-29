class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hash -> grouping ... {[a:1, b:1, c:1]: abc, bca,...}
        anagram_hash = {}
        str_hash = {}
        for i in strs:
            for j in i:
                if j not in str_hash.keys():
                    str_hash[j] = 1
                else:
                    str_hash[j] += 1
            
            elements = str(sorted(str_hash.items(), key = lambda x:x[0]))
            if elements not in anagram_hash.keys():
                anagram_hash[elements] = [i]
            else:
                anagram_hash[elements].append(i)
            str_hash = {}
        print(anagram_hash.values())
        return [i for i in anagram_hash.values()]



        

        