from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # columns:
            for i in range(9):
                nums=[]
                for k in range(9):
                    if board[i][k]!='.':
                        if board[i][k] in nums:
                            return False
                        else:
                            nums.append(board[i][k])
    # rows
            for i in range(9):
                nums = []
                for k in range(9):
                    if board[k][i] != '.':
                        if board[k][i] in nums:
                            return False
                        else:
                            nums.append(board[k][i])
    # squares
            for i in [0,3,6]:
                for k in [0,3,6]:
                    nums = []
                    for l in range(0,3):
                        for j in range(0,3):
                            if board[i + l][k + j] != '.':
                                if board[i+l][k+j] in nums:
                                    return False
                                else:
                                    nums.append(board[i+l][k+j])
            return True






board = [["5","3",".",".","7",".",".",".","."],
         ["6","3",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
ob1 = Solution()
print(ob1.isValidSudoku(board))
