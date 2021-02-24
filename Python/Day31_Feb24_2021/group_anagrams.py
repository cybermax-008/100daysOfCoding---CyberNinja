class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = {}
        for idx,ele in enumerate(strs):
            s_ele = ''.join(sorted(ele))
            if s_ele in h:
                h[s_ele].append(strs[idx])
            else:
                h[s_ele]=[strs[idx]]
        return h.values()