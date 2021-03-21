class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        h_map = {}
        for i,c in enumerate(s):
            if c in h_map:
                h_map[c]+=1
            else:
                h_map[c] = 1
        for i,c in enumerate(s):
            if h_map[c]==1:
                return i
        return -1