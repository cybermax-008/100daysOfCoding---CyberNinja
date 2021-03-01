from collections import Counter

def LetterCount(strParam):

    my_str = strParam.split()
    word_count = {}
    for word in my_str:
        word_lower = word.lower()
        if word not in word_count:
            letter_freq =  Counter(word_lower)
            word_count[word] = max(letter_freq.values())


    if max(word_count.values() == 1):
        return -1

    return sorted(word_count.items(),reverse=True, key= lambda x:x[1])[0][0]


print(LetterCount(input()))