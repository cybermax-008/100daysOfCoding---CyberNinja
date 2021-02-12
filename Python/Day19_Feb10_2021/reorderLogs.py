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