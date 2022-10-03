from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for k in range(i+1,len(nums)):
                if nums[i]+nums[k] == target:
                    return i,k




nums = [3,2,4]
target = 6
ob1 = Solution()
print(ob1.twoSum(nums,target))
