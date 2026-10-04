# lecture 42 : print matrix in spiral manner 

# leetcode 54

#matrix=[ [1,2,3,4,5,6] , [20,21,22,23,24,7] , [19,32,33,34,25,8] , [18,31,36,35,26,9], [17,30,29,28,27,10], [16,15,14,13,12,11] ]

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

n=len(matrix)
m=len(matrix[0])

top=0
bottom=n-1
left=0
right=m-1
l1=[]

while top<=bottom and left<=right:
    for i in range(left, right+1):
        l1.append(matrix[top][i])
    top+=1
    for i in range(top, bottom+1):
        l1.append(matrix[i][right])
    right-=1
    if top <= bottom:
        for i in range(right, left-1,-1):
            l1.append(matrix[bottom][i])
        bottom-=1
    if left <= right:
        for i in range(bottom, top-1, -1):
            l1.append(matrix[i][left])
        left+=1

print(l1)