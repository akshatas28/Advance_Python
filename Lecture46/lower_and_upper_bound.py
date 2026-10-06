# lecture 46 : Implememtation of Lower and Upper Bound

# below for lower bound

nums=[ 1,1,1,2,3,3,5,6,7,7,7,9,12,12,13 ]
target=3
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

# below for both lower and upper bound

nums=[ 1,1,1,2,3,3,5,6,7,7,7,9,12,12,13 ]
target=7
n=len(nums)
left=0
right=n-1
lb=n
ub=n
while left<=right:
    mid=(left+right)//2
    if nums[mid]>= target:
        if nums[mid]== target:
            lb=mid
            right=mid-1
        elif nums[mid]> target:
            ub=mid
            right=mid-1
    elif target>nums[mid]:
        left=mid+1
print(lb)
print(ub)