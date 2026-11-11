#lecture 52 - Find minimum in rotated sorted array II

#leetcode 154 - Find Minimum in Rotated Sorted Array II

nums = [2,2,2,0,1]
left=0
right=len(nums)-1
minnum = float("inf")
while left<=right:
    mid=(left+right)//2
    if nums[mid]==nums[left]==nums[right]:
        left+=1
        right-=1
    elif nums[mid]==nums[left] and nums[mid]!=nums[right]:
        left=mid+1
    elif nums[mid]==nums[right] and nums[mid]!=nums[left]:
        right=mid-1
    elif nums[mid]<nums[right]:
        right=mid-1
    else:
        left=mid+1
    minnum=min(minnum, nums[mid])
print(minnum)