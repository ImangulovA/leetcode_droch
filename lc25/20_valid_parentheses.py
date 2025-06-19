class Solution:
    def isValid(self, s: str) -> bool:
        opens = ["(","[","{"]
        closes = [")", "]", "}"]
        stack = []
        s = list(s)
        while s: 
            symb = s.pop(0)
            if symb in opens:
                stack += symb
            if symb in closes: 
                if stack == []:
                    return False
                opsymb = stack.pop(-1)
                if symb == "]":
                    if opsymb != "[":
                        return False
                if symb == ")":
                    if opsymb != "(":
                        return False
                if symb == "}":
                    if opsymb != "{":
                        return False
        return stack == []
    
    def isValidOptimized(self, s: str) -> bool:
        """
        Оптимизированное решение с использованием словаря для сопоставления скобок.
        Временная сложность: O(n), пространственная сложность: O(n)
        """
        brackets_map = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if not stack or stack.pop() != brackets_map[char]:
                    return False
        
        return len(stack) == 0