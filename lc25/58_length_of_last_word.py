class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        iterator = len(s) - 1
        word_started = False
        wl = 0
        while iterator >= 0:
            if word_started == False:
                if s[iterator] != ' ':
                    word_started = True
                    wl += 1
            else: 
                if s[iterator] != ' ':
                    wl += 1
                else:
                    return wl
            iterator -= 1
        return wl
    
    def lengthOfLastWordOptimized(self, s: str) -> int:
        """
        Оптимизированное решение с использованием встроенных методов Python.
        Временная сложность: O(n), пространственная сложность: O(1)
        """
        return len(s.strip().split()[-1]) if s.strip() else 0
    
    def lengthOfLastWordManual(self, s: str) -> int:
        """
        Ручная оптимизированная версия без встроенных методов.
        Временная сложность: O(n), пространственная сложность: O(1)
        """
        length = 0
        i = len(s) - 1
        
        # Пропускаем пробелы в конце
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Считаем длину последнего слова
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length
