class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        grp = {}
        
        for s in strings:
            patt = ()
            for i in range(len(s)):
                if i < len(s)-1:
                    c_diff = 26+ord(s[i])-ord(s[i+1])
                    patt+=(c_diff%26,)
            if patt not in grp:
                grp[patt] = [s]
            else:
                grp[patt].append(s)
        return grp.values()