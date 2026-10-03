# lecture 40 - Set Matrix zeros

# leetcode 73 - set matrix zeros

import copy
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix1=copy.deepcopy(matrix)
        
        zerorow=0
        zerocol=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix1[i][j]==0:
                    rowcount=0
                    colcount=0
                    zerorow=i
                    zerocol=j
                    while rowcount<len(matrix):
                        matrix[rowcount][zerocol]=0
                        rowcount+=1
                    while colcount<len(matrix[0]):
                        matrix[zerorow][colcount]=0
                        colcount+=1
        return matrix


# alternate best solution

matrix = [ [7,10,29,3] , [1,20,0,4] , [19,0,6,11] , [4,27,14,7] ]

row=len(matrix)
col=len(matrix[0])

rowtracker=[0]*row
coltracker=[[0]]*col

for i in range(row):
    for j in range(col):
        if matrix[i][j]==0:
            rowtracker[i]=-1
            coltracker[j]=-1
print(rowtracker, coltracker)

for i in range(row):
    for j in range(col):
        if rowtracker[i]==-1:
            matrix[i][j]=0
        if coltracker[j]==-1:
            matrix[i][j]=0
print(matrix)