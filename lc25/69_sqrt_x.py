class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        lb = 0
        rb = x
        while rb - lb > 1:
            k = (lb+rb)//2
            ksq = k*k
            if ksq == x:
                return k
            elif ksq > x:
                rb = k
            else:
                lb = k
        return lb