class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)
        maxArea = 0
        while(right-left>0):
            if height[left]<height[right-1]:
                h = height[left]
            else:
                h = height[right-1]
            w = right-left-1
            a = w*h
            if a>maxArea:
                maxArea=a
            if height[left]<height[right-1]:
                left+=1
            elif height[left]>height[right-1]:
                right-=1
            else:
                left+=1
                right-=1
        return maxArea