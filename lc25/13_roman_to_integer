class Solution:
    def romanToInt_better(self, s: str) -> int:
        # Более простое и эффективное решение
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Идем с конца строки
        for char in reversed(s):
            curr_value = roman_values[char]
            
            # Если текущее значение меньше предыдущего, вычитаем
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            
            prev_value = curr_value
        
        return total
    
    def romanToInt(self, s: str) -> int:
        rodict = {'I': 1,
        'V': 5, 
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900}
        difcheck = ['I', 'X', 'C']
        cases_difcheck = [['V','X'], ['L','C'], ['D','M']]
        ans = 0
        len_s = len(s)
        i = 0
        while i < len_s:
            added = False
            chi = s[i]
            for k in range(0,3):
                if chi == difcheck[k]:
                    if i+1 < len_s:
                        chi2 = s[i+1]
                        if chi2 in cases_difcheck[k]:
                            ans += rodict[chi+chi2]
                            i += 2
                            added = True
            if not added:
                ans += rodict[chi]
                i += 1
        return ans

