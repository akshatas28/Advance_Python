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
    