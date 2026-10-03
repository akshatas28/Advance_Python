#lecture: 37 - Rearrange array elements by sign

# leetcod   e 2149

nums = [5,10,-3,-1,-10,6]
newnums=[0]*len(nums)
positive=0
negative=1

for i in range(len(nums)):
    if nums[i]>0:
        newnums[positive]=nums[i]
        positive+=2
    elif nums[i]<0:
        newnums[negative]=nums[i]
        negative+=2


print(newnums)