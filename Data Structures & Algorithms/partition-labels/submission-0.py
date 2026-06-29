class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for idx, i in enumerate(s):
            last[i] = idx
        res = []
        length = end = 0
        for idx, i in enumerate(s):
            length += 1
            end = max(end, last[i])

            if idx == end:
                res.append(length)
                length = 0
        return res
            