# CCC 2011
# Problem J1: Which Alien?

numAntennas = int(input())
numEyes = int(input())

if numAntennas >= 3 and numEyes <= 4:
    print ("TroyMartian")
if numAntennas <= 6 and numEyes >= 2:
    print ("VladSaturnian")
if numAntennas <= 2 and numEyes <= 3:
    print ("GraemeMercuian")




