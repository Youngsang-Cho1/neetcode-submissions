class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ''
        longer_str = word1 if len(word1) > len(word2) else word2
        longer_len = max(len(word1), len(word2))
        shorter_len = min(len(word1), len(word2))
        for i in range(shorter_len):
            merged_str += word1[i] + word2[i]
        for j in range(shorter_len, longer_len):
            merged_str += longer_str[j]
        return merged_str

        