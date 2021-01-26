playlist = ["A","B","C","D","E"]

# Fucntion that does the shuffling operation
def shuffle(b,n):
    if b == 1:
        for i in range(n):
            first_song = playlist.pop(0)
            playlist.append(first_song)
        return
    elif b== 2:
        for i in range(n):
            last_song = playlist.pop()
            playlist.insert(0,last_song)
    elif b == 3:
        for i in range(n):
            playlist[0],playlist[1]=playlist[1],playlist[0]
    else:
        return 'Done'

# Main Program
while True:
    b = int(input("Button_number:"))
    n = int(input("Number of presses:"))
    control = shuffle(b,n)
    if control=='Done':
        break
print(' '.join(playlist))