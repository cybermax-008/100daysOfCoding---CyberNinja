class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grp = {}
        for i in strs:
            s_i = "".join(sorted(i))
            if s_i not in grp:
                grp[s_i] = [i]
            else:
                grp[s_i].append(i)
        return grp.values()
