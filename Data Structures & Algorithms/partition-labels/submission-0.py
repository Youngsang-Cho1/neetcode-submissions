from collections import Counter, defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # lowercase letters
        # as many substring as possible
        # each letter in only one substring
        # return list of ints w size of substrings
        res = []
        curr = 1
        original_counter = Counter(s)
        curr_counter = defaultdict(int)

        for i in range(len(s)):
            curr_counter[s[i]] += 1
            is_same = True
            for key, val in curr_counter.items():
                if curr_counter[key] != original_counter[key]:
                    is_same = False
                    break
            if is_same:
                res.append(curr)
                start = i
                curr = 0
            curr += 1

        if start == 0:
            res.append(len(s))
        
        return res



