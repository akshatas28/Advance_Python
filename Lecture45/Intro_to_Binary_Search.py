# lecture 45 : Intro to Binary Search

nums=[ 2,4,6,7,9,11,18,19 ]
target=13
n=len(nums)
left=0
right=n-1
while left<=right:
    mid=(left+right)//2
    if target<nums[mid]:
        right=mid-1
    elif target>nums[mid]:
        left=mid+1
    elif target==nums[mid]:
        print(mid)
        break
else:print(-1)


# using recursion

def binserach(left, right, mid, target, nums):
    if left>right:
        return -1
    if nums[mid]==target:
        return mid
    if nums[mid]>target:
        return binserach(left, mid-1, (left+right)//2, target, nums)
    if nums[mid]<target:
        return binserach(mid+1, right, (left+right)//2, target, nums)
    return binserach(left, right, (left+right)//2, target, nums)


nums=[ 2,4,6,7,9,11,18,19 ]
target=13
n=len(nums)
left=0
right=n-1
mid=(left+right)//2
print(binserach(left, right, mid, target, nums))

# tc : log(n) to the base 2

# sc for iterative is O(1) , for recursive is O(n)