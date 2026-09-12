class Solution:
    def reverse(self, x: int) -> int:
        temp = []
        res = ''
        str_x = str(x)
        is_neg = False
        for i in range(len(str_x) - 1, -1, -1):
            temp.append(str_x[i])
        if temp[-1] == '-':
            is_neg = True
            temp.pop()

        res = ''.join(temp)
        if not -(2**31) < (int(res)) <= (2**31) - 1:
            return 0

        return -int(res) if is_neg else int(res)
            