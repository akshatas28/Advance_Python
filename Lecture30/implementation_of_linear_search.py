# advanced python

# lect 30 : implementation of linear search

# simple : 

nums = [ 5,3,9,8,1,6,4,-10,-100 ]
#nums = [ 10,20,25,10,10,-5,-3,-2,-7 ]
#nums = [ 5,3,2,5,6,7,10,1 ]

i=0
target=4
while i <len(nums):
    if nums[i]==target:        
        break
    else:
        i+=1
print(i)


# one can attempt with recursion or for loop