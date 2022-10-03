from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix = [[i[k] for i in matrix[::-1]] for k in range(len(matrix))]
        # matrix = list(zip(*matrix[::-1]))
        # in-place solution from https://dev.to/seanpgallivan/solution-rotate-image-cpp#python-code
        n = len(matrix)
        depth = n // 2
        for i in range(depth):
            rlen, opp = n - 2 * i - 1, n - 1 - i
            for j in range(rlen):
                temp = matrix[i][i+j]
                matrix[i][i+j] = matrix[opp-j][i]
                matrix[opp-j][i] = matrix[opp][opp-j]
                matrix[opp][opp-j] = matrix[i+j][opp]
                matrix[i+j][opp] = temp
        #return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
ob1 = Solution()
print(ob1.rotate(matrix))
