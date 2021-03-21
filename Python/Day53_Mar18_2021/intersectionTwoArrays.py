class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h_map = {}
        res = []
        for i in nums1:
            h_map[i] =1
            
        for j in nums2:
            if j in h_map and h_map[j]:
                res.append(j)
                h_map[j]-=1
                
        return res
        