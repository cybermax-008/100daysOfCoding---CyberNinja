# CCC 2016
# Problem J5: Tandem Bicycle

questionType = int(input())
numPlayers = int(input())
DmojistanSpeed = [int(i) for i in input().split()]
PeglandSpeed = [int(i) for i in input().split()]
totalSpeed = 0
# For minimum speed combination
if questionType == 1:
    while(numPlayers>0):
        d = max(DmojistanSpeed)
        p = max(PeglandSpeed)
        DmojistanSpeed.remove(d)
        PeglandSpeed.remove(p)
        totalSpeed+=max(d,p)
        numPlayers-=1
else:
    while(numPlayers>0):
        d = max(DmojistanSpeed)
        p = min(PeglandSpeed)
        DmojistanSpeed.remove(d)
        PeglandSpeed.remove(p)
        totalSpeed+=max(d,p)
        numPlayers-=1
print(totalSpeed)