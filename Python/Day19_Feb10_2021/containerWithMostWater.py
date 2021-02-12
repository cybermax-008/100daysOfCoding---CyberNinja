class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height)-1
        max_area = 0
        
        while right-left > 0:
            h = height[left]
            if height[left]>height[right]:
                h = height[right]
                w = right-left
                right-=1
            elif height[left]<height[right]:
                h = height[left]
                w = right-left
                left+=1
            else:
                w = (right-left)
                left+=1
                right-=1
                
            a = w*h
            if max_area<a:
                max_area =a
                
        return max_area