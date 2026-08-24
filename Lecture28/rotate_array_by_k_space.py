# advanced python

# lect 28 : rotate array by k place

# simple : always reduce k to k%n : as when if k is equal to n then no need to rotate 

nums = [ 5,-2,3,9,0,6,10,7 ]
k=3
k=k%n
nums[:]= nums[-k:]  + nums[:-k]
print(nums)

# else

num = [ 5,-2,3,9,0,6,10,7 ]
k=k%n
for j in range(1, k+1):
    temp=nums[len(nums)-1]
    for i in range(len(nums)-2,-1,-1):
        nums[i+1]=nums[i]
    nums[0] = temp
print(nums)


# else

nums = [ 1,2 ]
k=3
for _ in range(0, k):
    temp=nums.pop(len(nums)-1)
    nums.insert(0, temp)
print(nums)

# leetcode pov : never print or return anything

# best solution

k=k%n
nums[:]= nums[-k:]  + nums[:-k]

# recursion with loop

nums = [ 5,-2,3,9,0,6,10,7 ]
#nums = [ 1,2 ]
k=3
left=0
right=len(nums)-1
def reverse(nums, left, right):
    while left<right:
        nums[left] , nums[right] = nums[right],nums[left]
        left+=1
        right-=1

reverse(nums, len(nums)-k, len(nums)-1)
reverse(nums, 0, len(nums)-k-1)
reverse(nums, 0 , len(nums)-1)

print(nums)