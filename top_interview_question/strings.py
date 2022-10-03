from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            tmp = s[i]
            s[i] = s[-1-i]
            s[-1-i]=tmp
        return s

    def reverse(self, x: int) -> int:
        xs = self.reverseString(list(str(x)))
        sign = 1
        if xs[-1] == '-':
            sign = -1
            xs = xs[:-1]
        n = sign*int(''.join(xs))
        if abs(n) > (2 ** 31 - 1):
            return 0
        return n

    def ourcounter(self, s: list) -> dict:
        counter = {}
        for el in s:
            if el in counter:
                counter[el]+=1
            else:
                counter[el]=1
        return counter

    def firstUniqChar(self, s: str) -> int:
        counter = self.ourcounter(list(s))
        for k,v in counter.items():
            if v == 1:
                return s.index(k)
        return -1

    def isAnagram(self, s: str, t: str) -> bool:
        return self.ourcounter(s) == self.ourcounter(t)

    def cleanstr(self, s:str) -> str:
        return ''.join(ch for ch in s.lower() if ch.isalnum())

    def isPalindrome(self, s: str) -> bool:
        s = self.cleanstr(s)
        for i in range(len(s)//2):
            if s[i]!=s[-1-i]:
                return False
        return True






s = ["H","a","n","n","a","h"]
s = "anagram"
t = "nagaram"
s = "A man, a plan, a canal: Panama"
ob1 = Solution()
# print(ob1.reverse(-123))
# print(ob1.firstUniqChar(s))
#
# print(ob1.ourcounter(list(s)))
# print(ob1.isAnagram(s,t))
# print(ob1.isPalindrome(s))
