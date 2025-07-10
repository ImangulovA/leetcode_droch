class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for k in range(len(triangle)-2, -1, -1):
            for i in range(0,len(triangle[k])):
                triangle[k][i] = triangle[k][i] + min(triangle[k+1][i],triangle[k+1][i+1])
        return triangle[0][0]