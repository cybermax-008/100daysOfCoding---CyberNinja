# find all triplets in the array where, a+b+c = 0. find all unique triplets.
def threeSum(nums):
    pos_list = []
    visited =[]
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i !=j and j!=k and i!=k:
                    temp = " ".join(sorted([str(nums[i]),str(nums[j]),str(nums[k])]))
                    if temp not in visited:
                        visited.append(temp)
                        if nums[i]+nums[j]+nums[k] ==0:
                            pos_list.append([nums[i],nums[j],nums[k]])
    return pos_list

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self,nums,i,res):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1