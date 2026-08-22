nums= [ 1,1,2 ]
expectedNums =[]
count=0
for i in range(len(nums)):
    if nums[i] in expectedNums:
        count+=1
    else: 
        expectedNums.append(nums[i])
    if i == len(nums)-1:
        expectedNums.extend(["_"] * count)
    k=len(nums)-count
print(f"{k}, nums = {expectedNums}")