# CCC 2014
# Problem J3: Double Dice

numRounds = int(input())
netPtAntonia = 100
netPtDavid = 100

for round in range(numRounds):
    roll = input().split()
    rollA = int(roll[0])
    rollD = int(roll[1])
    if rollA==rollD:
        continue
    elif rollA >rollD:
        netPtDavid-=rollA
    else:
        netPtAntonia-=rollD

print(netPtAntonia)
print(netPtDavid)