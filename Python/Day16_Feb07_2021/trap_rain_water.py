class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        area = 0
        left= []
        right= []
        left_max = 0
        right_max = 0
        for h in height:
            if h>left_max:
                left_max = h
            left.append(left_max)
        for h in height[::-1]:
            if h>right_max:
                right_max = h
            right.append(right_max)
        
        right =right[::-1]
        total_area = 0
        for l,r,h in zip(left,right,height):
            total_area += min(l,r)-h
        return total_area