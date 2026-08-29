# advanced python

# lect 32 : Find the missing number

# simple : 

nums = [1,0,3,4]

nums.sort()

i=0
j=0
while j < len(nums):
    if i ==nums[j]:
        i+=1
        j+=1
    else:
        print(i)
        break


# one can attempt with below

# Gauss summation

nums = [1,0,3,4]

print(sum(range(len(nums) + 1)) - sum(nums))

# else

for i in range(len(nums)+1):
    if i in nums:
        continue
    else:
        print(i)
        break

# else

d1={}

for i in range(0,len(nums)+1):
    d1[i]=0


for i in nums:
    d1[i]=1

for i in d1:
    if d1.get(i)==0:
        print(i)

# else

n=len(nums)
print(int(((n*(n+1))/2)-sum(nums)))