from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==0:
            return [1]
        elif digits[-1] < 9:
            digits[-1] += 1
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
        return digits

digits = [9,9,9]
ob1 = Solution()
print(ob1.plusOne(digits))
