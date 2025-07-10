class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.get(c,0) + 1
        return sum([i%2 == 1 for i in d.values()]) < 2