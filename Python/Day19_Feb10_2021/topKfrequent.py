class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mydict = {}
        for numbers in nums:
            if numbers not in mydict:
                mydict[numbers] = 0
            mydict[numbers] += 1

        mydict = sorted(mydict.items(), key=lambda x: x[1], reverse=True)

        ans = []
        while k > 0:
            ans.append(mydict[k-1][0])
            k -= 1
        return ans