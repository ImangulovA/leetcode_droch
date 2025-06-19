from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lb = 0
        rb = len(nums)
        if target <= nums[0]: 
            return 0
        while rb - lb > 1: 
            k = (rb+lb)//2
            if nums[k] >= target:
                rb = k
            else: 
                lb = k
        return rb
    
    def searchInsertOptimized(self, nums: List[int], target: int) -> int:
        """
        Оптимизированное решение с бинарным поиском.
        Временная сложность: O(log n), пространственная сложность: O(1)
        """
        left, right = 0, len(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left