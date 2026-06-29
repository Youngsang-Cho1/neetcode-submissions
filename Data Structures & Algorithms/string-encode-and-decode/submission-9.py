class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += i + '\n'
        return res


    def decode(self, s: str) -> List[str]:
        print(str)
        res = []
        res = s.split('\n')[:-1]
            
        return res
            
        
        