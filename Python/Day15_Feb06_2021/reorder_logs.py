class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        numeric_logs = []
        
        for log in logs:
            log_type = log.split(" ",1)[1]
            if log_type[0].isdigit():
                numeric_logs.append(log)
            else:
                letter_logs.append(log)
                
        letter_logs.sort(key= lambda log: log.split()[0])
        letter_logs.sort(key= lambda log: log.split()[1:])
        return letter_logs+numeric_logs

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)