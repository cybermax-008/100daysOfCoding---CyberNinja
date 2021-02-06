# Using Sliding window Brute force
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        maximum = 0
        while left<len(s) and right<len(s):
            subStr = s[left:right+1]
            if len(subStr)==len(set(subStr)):
                maximum = max(len(subStr),maximum)
            else:
                left+=1
            right+=1
        return maximum

# Using Sliding window : hash map
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        h = {}
        maximum = 0
        for right,c in enumerate(s):
            if c in h:
                left = max(left,h[c]+1)
            h[c] = right
            maximum = max(maximum,right-left+1)
        return maximum