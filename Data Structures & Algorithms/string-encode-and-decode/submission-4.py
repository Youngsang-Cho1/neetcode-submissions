class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for i in strs:
            encoded_str += i + '/'
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s != '':
            decoded_str = s.rstrip('/').split('/')
            return decoded_str
        else:
            return []
        
