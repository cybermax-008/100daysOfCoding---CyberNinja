    #Brute Force Method
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i]+nums[j]==target:
                        return [i,j]
                    
        return []
    
    #Using hasmap
    def twoSum(self, nums, target):
        h = {}
        for i,val in enumerate(nums):
            diff = target - val
            if diff in h:
                return [h[diff],i]
            h[val] = i