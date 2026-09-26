class Solution:
    def maxDifference(self, s: str) -> int:
        s_counter = Counter(s)
        max_odd_freq = 0
        min_even_freq = 101
        for ch, val in s_counter.items():
            if val % 2 == 0:
                min_even_freq = min(min_even_freq, val)
            else:
                max_odd_freq = max(max_odd_freq, val)

        return (max_odd_freq - min_even_freq)

        