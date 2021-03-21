class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 !=0:
            return False
        h_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        stack = []
        for i in s:
            if i in h_map and stack:
                if h_map[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True