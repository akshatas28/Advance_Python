# advanced python

# lect 34 : Two sums : leetcode 1

# simple : 

#nums=[ 5,9,1,2,4,15,6,3 ]
#nums=[ 2,7,11,15 ]
#nums=[ 3,2,4 ]
nums=[ 3,2,3 ]

target=6

for i in range(0,len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)


# else

d1={}
for i in range(0,len(nums)):
    remaining= target-nums[i]
    if remaining in d1:
        print(d1[remaining],i)
    d1[nums[i]] =i