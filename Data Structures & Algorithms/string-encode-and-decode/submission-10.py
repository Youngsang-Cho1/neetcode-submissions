class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')
        return ''.join(res)

    def decode(self, strs: str) -> List[str]:
        res = []
        i = 0
        while i < len(strs):
            j = i
            while strs[j] != '#':
                j += 1
            length = int(strs[i:j])
            i = j + 1
            j = i + length
            res.append(strs[i:j])
            i = j

        return res