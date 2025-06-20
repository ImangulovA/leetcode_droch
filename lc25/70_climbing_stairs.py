class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2: 
            return 2
        i, k = 1, 2
        for _ in range(2,n):
            i, k = k, i+k
        return k