class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(1, numRows):
            oa = ans[-1]
            ta = [oa[0]]
            for i in range(1, len(oa)):
                ta.append(oa[i]+oa[i-1])
            ta.append(oa[-1])
            ans.append(ta)
        return ans