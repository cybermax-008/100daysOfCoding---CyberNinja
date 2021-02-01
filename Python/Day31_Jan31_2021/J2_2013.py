# CCC 2013
# Problem J2: Rotating letters

rotatingLetters = ['I','O','S','H','Z','X','N']
word = input()
flag = 0
for letter in word:
    if not letter in rotatingLetters:
        print('NO')
        flag+=1
        break
if flag ==0:
    print('YES')

