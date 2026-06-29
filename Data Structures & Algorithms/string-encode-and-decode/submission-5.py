class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for i in strs:
            encoded_str += f"{len(i)}#{i}"
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        idx = 0
        decoded_str =[]
        while idx < len(s):
            slice_idx = s.find('#', idx)
            length = int(s[idx:slice_idx])
            print(length)
            decoded_str.append(s[slice_idx + 1: slice_idx + length + 1])
            idx = slice_idx + length + 1
        return(decoded_str)
        