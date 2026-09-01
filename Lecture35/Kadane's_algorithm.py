# advanced python

# lect 35 : Kadane's algorithm , Maximum sub array : leetcode 53

# simple : 


#nums=[ -2,1,-3,4,-1,2,1,-5,4 ]
#nums=[5,4,-1,7,8]
#nums=[-2,1]
#nums=[-2,-1]

#nums= for test case 202 on leetcode also this passes, but takes time

#output=6,23


total=float("-inf")

if len(nums)==1:
    print(nums[0])

for i in range(0,len(nums)):
    sum=nums[i]
    for j in range(i+1, len(nums)):
        if sum>total:
            total=sum
        sum+=nums[j]
    if sum>total:
        total=sum

print(total)

# bestest below


total=float("-inf")

if len(nums)==1:
    print(nums[0])

for i in range(0,1):
    sum=nums[i]
    for j in range(i+1, len(nums)):
        
        if sum>total:
            total=sum
        if sum<0:
            sum=0
        sum+=nums[j]
    if sum>total:
        total=sum

print(total)