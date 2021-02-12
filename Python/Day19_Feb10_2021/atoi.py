class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip()
        if len(s) ==0:
            return 0
        if s[0].isalpha():
            return 0
        elif s[0] == '-':
            sign = -1
        else:
            sign = 1
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        result = 0
        i = 0
        while i<len(s) and s[i].isdigit():
            result = result*10 + int(s[i])
            i+=1
        
        return max(-2**31,min(sign*result,2**31-1))