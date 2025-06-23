class Solution:
    def orig_val_pal(s: str) -> bool:
        lens = (len(s)-1) // 2 
        for i in range(0, lens):
            if s[i] != s[-i]:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        if self.orig_val_pal(s):
            return True
        for i in range(0, len(s)):
            if self.orig_val_pal(s[:i] + s[i+1:]):
                return True
        return False