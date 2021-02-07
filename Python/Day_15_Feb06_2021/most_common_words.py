class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = []
        temp = ''
        s = paragraph.strip()
        for i in range(len(s)):
            if s[i].isalpha():
                temp+=s[i]
            else:
                if len(temp)>0:
                    temp=temp.lower().strip()
                    if temp not in banned:
                        words.append(temp)
                    temp=''
        if len(temp)>0:
            words.append(temp.lower())
        print(words)
        h = {}
        for word in words:
            if word not in h:
                h[word]=1
            else:
                h[word]+=1
        max_freq = max(h.values())
        for k,v in h.items():
            if v==max_freq:
                return k

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word_count = defaultdict(int)
        max_count = 0
        ans = ""
        word_buffer = []
        
        for i,c in enumerate(paragraph):
            if c.isalnum():
                word_buffer.append(c.lower())
                if i != len(paragraph)-1:
                    continue
            if len(word_buffer)>0:
                word = ''.join(word_buffer)
                if not word in banned:
                    word_count[word]+=1
                    if word_count[word]>max_count:
                        max_count = word_count[word]
                        ans = word
            word_buffer = []
            
        return ans