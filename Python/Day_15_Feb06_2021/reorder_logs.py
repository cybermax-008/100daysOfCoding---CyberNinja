class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs, digit_logs = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        print(letter_logs,digit_logs)
        
        letter_logs.sort(key = lambda x:x.split()[0])
        letter_logs.sort(key = lambda x:x.split()[1:])
        return letter_logs+digit_logs

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)