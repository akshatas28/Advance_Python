# lecture 43 : three sum

# leetcode 15

nums=[ -1, 0,1,2,-1,-4 ]

n=len(nums)
s1=set()

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if nums[i]+nums[j]+nums[k]==0:
                l1=[nums[i], nums[j],nums[k] ]
                l1.sort()
                s1.add(tuple(l1))
                l1[:]=[]
print([list(t) for t in s1])

# for above code - timeout exceeded error is recieved

nums=[ -1, 0,1,2,-1,-4 ]
nums.sort()
n=len(nums)
result=[]

for i in range(n-2):
    if i>0 and nums[i]==nums[i-1]:
        continue
    left=i+1
    right=n-1
    while left<right:
        currentsum=nums[i]+nums[left]+nums[right]
        if currentsum==0:
            result.append([nums[i],nums[left],nums[right]])
            left+=1
            right-=1
            while left < right and nums[left] == nums[left - 1]:
                left+=1
            while left < right and nums[right] == nums[right + 1]:
                right-=1
        elif currentsum<0:
            left+=1
        else:
            right-=1

print(result)

# alternate below

nums=[ -1, 0,1,2,-1,-4 ]

n=len(nums)
s1=set()
l1=[]

for i in range(0,n-1):
    s2=set()
    for j in range (i+1, n):
        finalint=(-(nums[i]+nums[j]))
        if finalint in s2:
            s2.add(nums[j])
            l1=[nums[i], nums[j],finalint ]
            l1.sort()
            s1.add(tuple(l1))
        else:
            s2.add(nums[j])

print([list(t) for t in s1])