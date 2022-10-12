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


    def myAtoi(self, s: str) -> int:
        s = list(s)
        a = 0
        sign = 1
        signm = False
        while len(s) > 0:
            if s[0] == ' ':
                if signm == True:
                    return 0
                s.pop(0)
            elif s[0] == '+':
                if signm == True:
                    return 0
                s.pop(0)
                signm = True
            elif s[0] == '-':
                if signm == True:
                    return 0
                s.pop(0)
                sign = -1
                signm = True
            elif (s[0] >= '0') & (s[0] <= '9'):
                    while (s[0] >= '0') & (s[0] <= '9'):
                        a = a*10 + int(s[0])
                        s.pop(0)
                        if a > (2 ** 31 - 1):
                            if sign == 1:
                                return 2 ** 31 - 1
                            else:
                                return - 2 ** 31
                        if len(s) == 0:
                            break
                    return a*sign
            else:
                return 0
        return 0

    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)
        if ln > lh:
            return -1
        if ln == 0:
            return -1
        if lh == 0:
            return -1
        for k in range(lh-ln+1):
            if haystack[k]==needle[0]:
                sfsg = True
                for l in range(1,ln):
                    if haystack[k+l] != needle[l]:
                        sfsg = False
                        break
                if sfsg:
                    return k
        return -1

    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        if len(strs)==0:
            return lcp
        lcpcont = True
        chrnum = 0
        while lcpcont:
            try:
                ch = strs[0][chrnum]
                for s in strs[1:]:
                    if s[chrnum] != ch:
                        lcpcont = False
                        return lcp
                lcp += ch
                chrnum += 1
            except:
                return lcp






# s = ["H","a","n","n","a","h"]
# s = "anagram"
# t = "nagaram"
# s = "A man, a plan, a canal: Panama"
# s = "   +-42sfdgergh"
# t = '       '
# haystack = "saqwdbutsadssssssssssssssss"
# needle = "ssssssss"
strs = ["flower", "f", "fwerlight"]
ob1 = Solution()
# print(ob1.reverse(-123))
# print(ob1.firstUniqChar(s))
#
# print(ob1.ourcounter(list(s)))
# print(ob1.isAnagram(s,t))
# print(ob1.isPalindrome(s))
# print(ob1.myAtoi(s))
# print(ob1.strStr(haystack, needle))
print(ob1.longestCommonPrefix(strs))