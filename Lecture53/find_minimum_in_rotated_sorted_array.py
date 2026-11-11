#lecture 53 - Find minimum in rotated sorted array
#leetcode 153
nums = [4,5,6,7,0,1,2]
nums=[7,8,1,2,3,4,5,6]
minnum = float("inf")
for i in range(len(nums)):
    minnum=min(minnum, nums[i])
    print(minnum)

#second solution

nums = [4,5,6,7,0,1,2]
nums=[7,8,1,2,3,4,5,6]
left=0
right=len(nums)-1
minnum = float("inf")
while left<=right:
    mid=(left+right)//2
    if nums[mid]<nums[right]:
        right=mid-1
    elif nums[mid]>nums[right]:
        left=mid+1
    elif nums[mid]<nums[left]:
        right=mid-1
    else:
        left=mid+1
    minnum=min(minnum, nums[mid])
print(minnum)

#more optimal

nums = [4,5,6,7,0,1,2]
nums=[7,8,1,2,3,4,5,6]
left=0
right=len(nums)-1
minnum = float("inf")
while left<=right:
    mid=(left+right)//2
    if nums[mid]<nums[right]:
        right=mid-1
    else:
        left=mid+1
    minnum=min(minnum, nums[mid])
print(minnum)