class Solution(object):
    def twoSum(self, nums, target):
        ind =0
        newnums=[]
        def solve(ind,newnums):
            
            if (ind==len(nums)):
                return
            m = target - nums[ind]
            if m in nums:
                if ind != nums.index(m):
                    t = nums.index(m)
                    newnums.append(ind)
                    newnums.append(t)
                    return (newnums)
                else:
                    return solve (ind+1, newnums)
            else:
                return solve (ind+1, newnums)
        return solve (ind+1, newnums)
    