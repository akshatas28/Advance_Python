# advanced python

# lect 33 : MAX CONSECUTIVE ONES : leetcode 485

# simple : 

nums = [ 1,1,0,1,0,1,1,1,1,0,1,1 ]

i=0
count=0
l1=[]
for i in range(len(nums)):
    if nums[i]!=1:
        count=0
    else:
        count+=1
    l1.append(count)

print(max(l1))

# else

maxcount=0
count=0
i=0
while i<len(nums):
    if nums[i]==1:
        count+=1
        i+=1
    else:
        count=0
        i+=1
    if count>maxcount:
        maxcount=count
    
print(maxcount)

# else

# class comes here
    # def comes here
        i=0
        count=0
        l1=[]
        while i<len(nums):
            if nums[i]!=1:
                count=0
                i+=1
            elif nums[i]==1:
                count+=1
                i+=1
            l1.append(count)
         return (max(l1))