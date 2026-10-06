# lecture 47 : Insert Search Position

# leetcode : 35

nums=[ 1,3,4,5,8,9,14,15,19,20,21 ]
target=5
n=len(nums)
left=0
right=n-1
lb=n
while left<=right:
    mid=(left+right)//2
    if nums[mid]>= target:
        lb=mid
        right=mid-1
    elif target>nums[mid]:
        left=mid+1
print(lb)