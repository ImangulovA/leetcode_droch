from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        ans = ""
        i = 0
        k = len(strs)
        shortest_len = min([len(x) for x in strs])
        keepon = True
        while keepon:
            checktoadd = strs[0][i]
            for j in range(1,k):
                if strs[j][i] != checktoadd:
                    keepon = False
                    break
            if keepon:
                i += 1
                ans += checktoadd
            if i == shortest_len:
                keepon = False
        return ans

    def longestCommonPrefixOptimized(self, strs: List[str]) -> str:
        # Более эффективная проверка пустых строк
        if not strs or any(not s for s in strs):
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        # Используем первую строку как эталон
        first = strs[0]
        shortest_len = min(len(s) for s in strs)
        
        # Ищем общий префикс
        for i in range(shortest_len):
            char = first[i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return first[:i]
        
        return first[:shortest_len]

    def longestCommonPrefixWithZip(self, strs: List[str]) -> str:
        # Альтернативный подход с использованием zip()
        if not strs:
            return ""
        
        # Используем zip для параллельного итерирования
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) != 1:
                return strs[0][:i]
        
        return min(strs, key=len)

        