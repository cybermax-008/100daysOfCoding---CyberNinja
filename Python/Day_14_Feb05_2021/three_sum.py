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

print(threeSum([-1,0,1,2,-1,-4]))