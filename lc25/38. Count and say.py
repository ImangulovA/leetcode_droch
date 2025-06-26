class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        while n > 1:
            news = ""
            ch = s[0]
            cntr = 1
            for chars in s[1:]:
                if ch == chars:
                    cntr += 1
                else:
                    news += str(cntr)
                    news += ch  
                    ch = chars
                    cntr = 1                 
            news += str(cntr)
            news += ch    
            n -= 1
            s = news
        return s