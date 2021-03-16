def load_word():
    with open('english-words/words_alpha.txt') as txt_file:
        all_words = list(txt_file.read().split())
    return all_words

def search_word(query_word,dictionary):
    mid = 0
    start = 0
    end = len(dictionary)
    step = 0

    while start<= end:
        step+=1
        mid =  (start+end )//2
        if query_word == dictionary[mid]:
            return dictionary[mid]
        if query_word < dictionary[mid]:
            end = mid -1
        else:
            start = mid + 1
    return 'Incorrect word given as query   !'

words = load_word()
print(search_word('tige',words))
