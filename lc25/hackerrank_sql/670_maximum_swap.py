from math import pow
class Solution:
    def maximumSwap(self, num: int) -> int:
        nlist = list(map(int,list(str(num))))
        mdelta = 0
        mik = [0,0]
        for i in range(0, len(nlist)-1):
            for k in range(i + 1, len(nlist)):
                if nlist[i] < nlist[k]:
                    delta = (nlist[k]-nlist[i]) * pow(10, k) + (nlist[i] - nlist[k]) * pow(10, i)
                    if delta > mdelta:
                        mdelta = delta
                        mik = [i,k]
                        print(delta,i,k)
        return num + delta