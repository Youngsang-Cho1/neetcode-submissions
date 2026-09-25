from collections import Counter, defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        curr = 1
        original_counter = Counter(s)
        seen = set()
        remaining = 0

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                remaining += original_counter[s[i]]
            remaining -= 1

            if remaining == 0:
                res.append(curr)
                curr = 0
            
            curr += 1

        return res



