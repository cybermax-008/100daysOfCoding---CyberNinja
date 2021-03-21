class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in visited:
                return [i,visited[diff]]
            visited[n] = i
            
        return []