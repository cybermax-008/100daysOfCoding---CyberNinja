characters = [['A','B','C','D','E','F'],
              ['G','H','I','J','K','L'],
              ['M','N','O','P','Q','R'],
              ['S','T','U','V','W','X'],
              ['Y','Z','space','-','.','enter']]

def find(target):
    if target == ' ':
        target = 'space'
    if target == '\n':
        target = 'enter'
    for i,row in enumerate(characters):
        for j,char in enumerate(row):
            if char == target:
                return (i,j)
    return (None,None)

# Input
inputString = list(input().upper())
inputString.append('\n')

total_moves = 0
current_loc = (0,0)
for letter in inputString:
    x,y = find(letter)
    print("cuure:",current_loc)
    print(letter,x,y)
    total_moves = total_moves + abs(x-current_loc[0])+abs(y-current_loc[1])
    current_loc = (x,y)
#Output 
print(total_moves)
