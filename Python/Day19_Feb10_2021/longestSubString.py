# # Using Sliding window and Set
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        
#         left = 0
#         right = 0
#         max_len = 0
#         while right < len(s):
#             sub = s[left:right+1]
#             print(sub)
#             if len(sub) == len(set(sub)):
#                 if max_len < len(set(sub)):
#                     max_len = len(set(sub))
#             else:
#                 left +=1
#             print(max_len)
#             right+=1
#         return max_len
    
# Using Sliding window with hashmap

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        h = {}
        max_len = 0
        left = 0
        for right,c in enumerate(s):
            if c in h:
                left = max(left,h[c]+1)
            
            h[c] = right
            max_len = max(max_len,right - left+1)
            
        return max_len