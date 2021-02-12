#My solution
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        if not paragraph:
            return ""
        temp = ""
        words = []
        for c in paragraph:
            if c.isalnum():
                temp+=c.lower()
            else:
                if len(temp)>0:
                    words.append(temp)
                temp=""
        if len(temp)>0:
            words.append(temp)
        valid_words = [word for word in words if word not in banned]
        return max(valid_words,key=valid_words.count)

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word_count = defaultdict(int)
        
        word_buffer = []
        max_count = 0
        ans = ''
        for i in paragraph:
            if i.isalnum():
                word_buffer.append(i.lower())
                if paragraph.index(i) != len(paragraph)-1:
                    continue
            if len(word_buffer)>0:
                word = ''.join(word_buffer)
                if word not in banned:
                    word_count[word]+=1
                if word_count[word]>max_count:
                    max_count = word_count[word]
                    ans = word
            word_buffer = []
            
        return ans