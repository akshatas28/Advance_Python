# lecture 50 : count the occurences of the number

nums=[ 1,2,3,3,3,3,3,5,6,8,9,9,10 ]
target=3

#nums=[ 5,7,7,8,8,10 ]
#target=6

n=len(nums)
left=0
right=n-1
lb=-1
ub=-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]>= target:
        if nums[mid]== target and right==n-1:
            ub=mid
            right+=1
        elif nums[mid]== target:
            lb=mid
            right=mid-1
        elif nums[mid]> target:
            ub=mid
            right=mid-1
    elif target>nums[mid]:
        left=mid+1
if lb==-1:
    print("0")
else:
    print(ub-lb+1)