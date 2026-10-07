class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = {}
        curr = n
        while curr != 1:
            curr = sum([(int(i)**2) for i in str(curr)])
            print(curr)
            if curr not in hashmap:
                hashmap[curr] = 1
            else:
                break
        return curr == 1
        



        