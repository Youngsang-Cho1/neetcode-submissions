class Solution:
    def myPow(self, x: float, n: int) -> float:
        new_x = 1
        for i in range(abs(n)):
            if n>0:
                new_x *= x 
            else:
                new_x = new_x / x
            print(new_x)
        return new_x
        