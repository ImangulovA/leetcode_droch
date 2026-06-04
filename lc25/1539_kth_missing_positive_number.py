# 1539. Kth Missing Positive Number
# Linear scan over gaps: between arr[i-1] and arr[i] there are d missing numbers.
# Burn down k across the gaps; when a gap is big enough, the answer sits inside it.
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        if arr[0] > 1:
            k = k - arr[0] + 1
        #print(k)
        for i in range(1, len(arr)):
            d = arr[i] - arr[i-1] - 1
            #print(i,arr[i],d,k)
            if d >= k:
                return arr[i-1] + k
            else:
                k = k - d
        return arr[-1] + k
