class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def dictisation_letters(s):
            sd = {}
            for i, char in enumerate(s):
                if char not in sd:
                    sd[char] = [i]
                else:
                    sd[char].append(i)
            return sorted(sd.values())
        sv = dictisation_letters(s) 
        tv = dictisation_letters(t)
        return sv == tv