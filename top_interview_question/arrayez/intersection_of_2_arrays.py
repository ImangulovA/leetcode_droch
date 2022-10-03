from typing import List

#  Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        nums3 = []

        for n in nums2:
            if n in nums1:
                nums3.append(n)
                nums1 = nums1[(nums1.index(n)+1):]
                if len(nums1) == 0:
                    return nums3

        return nums3

nums = [1, 2, 2, 1]
numst = [2,2]
ob1 = Solution()
print(ob1.intersect(nums,numst))

