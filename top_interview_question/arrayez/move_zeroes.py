from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        for n in range(len(nums)-1,-1,-1):
            if nums[n] == 0:
                c+=1
                nums.pop(n)
        nums += [0]*c



nums = [9,0,0,0,0,9,9,0,0]
nums =  [0,1,0,3,12]
ob1 = Solution()
print(ob1.moveZeroes(nums))
