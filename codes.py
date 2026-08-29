index=0
#replace with underscores
for j in range(1, len(num)):
    if num[j] !=num[index]:
        index+=1
        num[index] , num[j] = num[j] , num[index]

num[index+1:] = ["_"] * (len(num)-1-index)
print(index)

# alternate solution
num[:] = num[-value:]+num[0:len(num)-value]
print(num)

# reverse an array
def reversearray(nums, value, i, temp):
    if i == -1:
        nums[0]=temp
        return reversearray(nums, value+1, len(nums)-2, nums[len(nums)-1])
    if value==k+1:
        return nums
    if value!=0:
        nums[i+1] = nums[i]
        return reversearray(nums, value, i-1, temp)

i=0
count=0
l1=[]
while i<len(nums):
    if nums[i]!=1:
        count=0
        i+=1
    elif nums[i]==1:
        count+=1
        i+=1
        l1.append(count)
return (max(l1))

maxcount=0
count=0
i=0
while i<len(nums):
    if nums[i]==1:
        count+=1
        i+=1
    elif nums[i]!=1:
        if count>maxcount:
            maxcount=count
        count=0
        i+=1
print(maxcount)


st=str(x)

if x<0:
    p=(int(st[::-1].strip('-')))
    if p<=((2**31)-1) and p>=(-(2**31)):
        print(-p)
else:
    p=(int(st[::-1]))
    if x<=((2**31)-1) and x>=(-(2**31)):
        print(p)

class Solution:
    def reverse(self, x: int) -> int:
        st=str(x)

        if x<0:
            p=(int(st[::-1].strip('-')))
            if p<=((2**31)-1) and p>=(-(2**31)):
                return (-p)
            else:
                return 0
        else:
            p=(int(st[::-1]))
            if p<=((2**31)-1) and p>=(-(2**31)):
                return (p)
            else:
                return 0