# lecture 41 - Rotate matrix by 90 degree

# leetcode 48 - rotate image

import copy
    
matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16] ]

matrix1=copy.deepcopy(matrix)

i1=0
j = len(matrix[0])-1

while i1<len(matrix):
    i=0
    j1=0
    while i<len(matrix[0]):
        matrix[i][j]=matrix1[i1][j1]
        i+=1
        j1+=1
    i1+=1
    j-=1

print(matrix)


# alternate

matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16] ]
n=len(matrix)

for i in range(0,n-1):
    for j in range(i+1,n):
        matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
for i in range(0,n):
    matrix[i].reverse()
print(matrix)