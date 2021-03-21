class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uni_id = set()
        for idd in emails:
            local,domain = idd.split('@')
            local = "".join(local.split('+')[0].split('.'))
            f_email = local+'@'+domain
            uni_id.add(f_email)
            
        return len(uni_id)