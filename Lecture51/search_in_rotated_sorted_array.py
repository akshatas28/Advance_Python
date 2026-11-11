#lecture 51 - search in rotated sorted array
#leetcode 33
#nums=[11,15,20,1,4,5,6,8,9,10]
#target = 15 # 9
nums=[4,5,6,7,0,1,2]
target=0
n=len(nums)
z=-1
for i in range(n):
    if nums[i]==target:
        z=i
if z!=(-1):
    print(z)
else:
    print(-1)


#above code is for O(n)
#below with O(n)

left=0
right=n-1
intfound=-1
while left<right:
    if nums[left]==target:
        intfound=left
        break
    elif nums[right]==target:
        intfound=right
        break
    left+=1
    right-=1
if intfound!=(-1):
    print(intfound)
else:
    print(-1)


# next solution --> O(log n)

#nums=[11,15,20,1,4,5,6,8,9,10]
#target = 15 # 9
nums=[4,5,6,7,0,1,2]
target=0
n=len(nums)
left1=0
right1=n-1
ans=-1
while left1<=right1:
    mid=(left1+right1)//2
    if nums[mid]==target:
        ans=mid
        break
    elif nums[mid]<nums[right1]:
        if nums[right1]>=target and target>=nums[mid]:
            left1=mid+1
        else:
            right1=mid-1
    else:
        if nums[left1]<=target and target<=nums[mid]:
            right1=mid-1
        else:
            left1=mid+1
if ans!=(-1):
    print(ans)
else:
    print(-1)