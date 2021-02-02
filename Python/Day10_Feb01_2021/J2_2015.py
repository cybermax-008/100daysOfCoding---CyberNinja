# CCC 2015
# Problem J2: Happy or Sad

message = input()

def emotions(message):
    head = message.count(':-')
    if head == 0:
        return 'none'
    smile = message.count(')')
    sad = message.count('(')
    if head != smile+sad:
        return 'none'
    else:
        if smile>sad:
            return 'happy'
        else:
            return 'sad'
print(emotions(message))