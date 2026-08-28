# advanced python

# lect 29 : Move zeros to the end of this list

# simple : 

nums = [ 1,0,2,4,3,0,0,3,5 ]
count=0
i=0
n=len(nums)
while i <n:
    if nums[i]==0:
        count+=1
        nums.pop(i)
        n-=1
    else:
        i+=1

nums.extend([0]*count)
print(nums)

# below one can be tried but avoid 

nums = [ 1,0,2,4,3,0,0,3,5 ]

left =0
right=len(nums)-1

while left<=right:
    if nums[left]==0 and nums[right]!=0:
        nums[left], nums[right] = nums[right], nums[left]
        left+=1
        right-=1
    elif nums[left]!=0 and nums[right]==0:
        left+=1
        right-=1
    elif nums[left]!=0 and nums[right]!=0:
        left+=1
    elif nums[left]==0 and nums[right]==0:
        right-=1

print(nums)


# else

nums = [ 1,0,2,4,3,0,0,3,5 ]
n=len(nums)
temp=[]
for i in range(len(nums)):
    if nums[i]!=0:
        temp.append(nums[i])
nums[:]=temp
nums.extend([0]*(n-len(temp)))
print(nums)

# leetcode pov : never print or return anything

nums = [ 1,0,2,4,3,0,0,3,5 ]
n=len(nums)
i=0
j=1
while j <n:
    if nums[i]==0:
        if nums[j]==0:
            j+=1
        elif nums[j]!=0:
            nums[i] , nums[j] = nums[j] , nums[i]
            i+=1
            j+=1
    else:
        i+=1
        j+=1

print(nums)