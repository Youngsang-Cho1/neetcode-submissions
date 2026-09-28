class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        for i in strs:
            item = ''.join(sorted(i))
            if item not in hashmap:
                hashmap[item] = [i]
            else:
                hashmap[item].append(i)

        for key, value in hashmap.items():
            res.append(value)
        return res

            
            