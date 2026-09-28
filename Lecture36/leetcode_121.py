#lect 36 - Best time to buy and sell - Max Profit
#leetcode - 121

# below solution fails for few cases

#nums = [7,2,1,5,6,4,8]
#nums=[8,5,3,2,1]
nums=[2,4,1]
 
low = float("inf")
high = float("-inf")
 
for i in range(0,len(nums)):
    if nums[i]<low:
        low=nums[i]
for i in range(nums.index(low), len(nums)):
    if nums[i]>high:
        high=nums[i]
if nums.index(high)==0:
    print(0)
else:
    print(high-low)


# alternate solution : this works for all

#nums=[8,5,3,2,1]

low = float("inf")
profit=0
for i in range(0,len(nums)):
    low=min(low,nums[i])
    profit=max(profit, nums[i]-low)
 
print(profit)