class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        oa = [1]
        for _ in range(0, rowIndex):
            ta = [oa[0]]
            for i in range(1, len(oa)):
                ta.append(oa[i]+oa[i-1])
            ta.append(oa[-1])
            oa = ta
        return oa