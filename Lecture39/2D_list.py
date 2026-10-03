# lecture 39 : learn about 2D list and matrix

nums=[ [5,20,3] , [7,-10,9] , [1,-52,6] ]

for i in (nums):
    for j in (i):
        print(j)

# alternate

nums=[ [5,20,3] , [7,-10,9] , [1,-52,6] ]

for i in (nums):
    for j in (i):
        print(j , end=" ")
    print()

# print upper triangle

for i in range(len(nums)):
    for j in range(len(nums[0])):
        if j>=i:
            print(nums[i][j],end=" " )
        # else one can print 0
        else:
            print(0,end=" "  )
    print()

# print lower triangle

for i in range(len(nums)):
    for j in range(len(nums[0])):
        if j<=i:
            print(nums[i][j],end=" " )
        # else one can print 0
        else:
            print(0,end=" "  )
    print()

# print diagonal triangle

for i in range(len(nums)):
    for j in range(len(nums[0])):
        if j==i:
            print(nums[i][j],end=" " )
        # else one can print 0
        else:
            print(0,end=" "  )
    print()

# print reverse diagonal triangle

for i in range(len(nums)):
    for j in range(len(nums[0])):
        if ((j+i) == len(nums[0])-1):
            print(nums[i][j],end=" " )
        # else one can print 0
        else:
            print(0,end=" "  )
    print()

# transpose

for i in range(len(nums)):
    for j in range(len(nums[0])):
        print(nums[j][i],end=" " ) 
    print()

# alternate : the bestest

nums1=[ [5,9,1] , [2,3,7] ]
rows=len(nums1)
cols=len(nums1[0])
for i in range(cols):
    for j in range(rows):
        print(nums1[j][i],end=" " ) 
    print()