# lecture 44 : 4 sum

# leetcode 18

nums=[ 1,0,-1,0,-2,2 ]
target=0

n=len(nums)
s1=set()
l1=[]

for i in range(n-3):
    for j in range(i+1,n-2):
        for k in range(j+1,n-1):
            for l in range(k+1, n):
                if nums[i]+nums[j]+nums[k]+nums[l]==target:
                    l1=[nums[i], nums[j],nums[k], nums[l]]
                    l1.sort()
                    s1.add(tuple(l1))

print([list(t) for t in s1])

# for above code - timeout exceeded error is received

#nums=[ 1,0,-1,0,-2,2 ]
#target=0

nums=[-2,-1,-1,1,1,2,2]
target=0
#nums=[ 2,2,2,2,2 ]
#target=8

nums.sort()
n=len(nums)
result=[]

for j in range(n-3):
    if j>0 and nums[j]==nums[j-1]:
        continue
    for i in range(j+1,n-2):
        if i>j+1 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=n-1
        while left<right:
            currentsum=nums[j]+nums[i]+nums[left]+nums[right]
            if currentsum==target:
                result.append([nums[j],nums[i],nums[left],nums[right]])
                left+=1
                right-=1
                while left < right and nums[left] == nums[left - 1]:
                    left+=1
                while left < right and nums[right] == nums[right + 1]:
                    right-=1
            elif currentsum<target:
                left+=1
            else:
                right-=1

print(result)

# alternate below

#nums=[ 1,0,-1,0,-2,2 ]
#target=0

#nums=[-2,-1,-1,1,1,2,2]
#target=0
nums=[ 2,2,2,2,2 ]
target=8

n=len(nums)
s1=set()
l1=[]

for k in range(0, n-2):
    for i in range(k+1,n-1):
        s2=set()
        for j in range (i+1, n):
            finalint=(target-(nums[k]+nums[i]+nums[j]))
            if finalint in s2:
                s2.add(nums[j])
                l1=[nums[k],nums[i], nums[j],finalint ]
                l1.sort()
                s1.add(tuple(l1))
            else:
                s2.add(nums[j])

print([list(t) for t in s1])