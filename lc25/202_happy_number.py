from math import pow
class Solution:
    def isHappy(self, n: int) -> bool:
        prevsteps = set()
        prevsteps.add(n)
        def hfation(n): 
            ans = 0
            while n:
                ans += pow(n%10, 2)
                n = n//10
            return ans
        while True:
            n = hfation(n)
            if n not in prevsteps: 
                prevsteps.add(n)
            else:
                if n == 1:
                    return True
                else: 
                    return False