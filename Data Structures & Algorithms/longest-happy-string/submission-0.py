class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        stack = ''
        hashmap = {'a' : a, 'b': b, 'c': c}
        counter = a + b + c
        while counter > 0:
            map_sorted = list(sorted(hashmap.items(), key = lambda x:x[1], reverse = True))
            first, first_count = map_sorted[0]
            second, second_count = map_sorted[1]
            third, third_count = map_sorted[2]

            if stack[-2:].count(first) != 2 and first_count:
                stack += first
                hashmap[first] -= 1
            elif stack[-2:].count(second) != 2 and second_count:
                stack += second
                hashmap[second] -= 1
            elif stack[-2:].count(third) != 2 and third_count:
                stack += third
                hashmap[third] -= 1
            counter -= 1
        return stack

            




        