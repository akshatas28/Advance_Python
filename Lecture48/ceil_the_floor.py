# lecture 48 : ceil the floor

# codeninjas and naukri question

nums=[ 3,4,4,4,8,9,9,10,12,12,14,15 ]
target=20
n=len(nums)
left=0
right=n-1
lb=-1
ub=-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]>= target:
        if nums[mid]== target:
            lb=mid
            ub=mid
            right=mid-1
        elif nums[mid]> target:
            ub=mid
            right=mid-1
    elif nums[mid]<target:
        lb=mid
        left=mid+1

print(nums[lb] if lb!=-1 else -1)
print(nums[ub] if ub!=-1 else -1)