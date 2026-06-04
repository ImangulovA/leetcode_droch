# 2530. Maximal Score After Applying K Operations
# Greedy: always take the current max, add it to the score, and push back
# ceil(x/3). Kept as a sorted list with bisect.insort instead of a max-heap.
import math
import bisect
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        nums.sort()
        for _ in range(k):
            a = nums.pop()
            score += a
            bisect.insort(nums, math.ceil(a / 3))
        return score
