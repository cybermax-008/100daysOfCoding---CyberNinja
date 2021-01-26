def catch_fish(troutPt,pikePt,pickerelPt,totalPt):
    totalTrout = totalPt//troutPt
    totalPike = totalPt//pikePt
    totalPickerel = totalPt//pickerelPt
    fishList = []
    for i in range(totalTrout+1):
        for j in range(totalPike+1):
            for k in range(totalPickerel+1):
                if troutPt*i+pikePt*j+pickerelPt*k <= totalPt:
                    if i+j+k >0:
                        fishList.append([i,j,k])
    return fishList




troutPt = int(input())
pikePt = int(input())
pickerelPt = int(input())
totalPt = int(input())
fishList = catch_fish(troutPt,pikePt,pickerelPt,totalPt)

for i,j,k in fishList:
    print(str(i),"Brown Trout,",str(j),"Northern Pike,",str(k),"Yellow pickerel")
print("Number of ways to catch fish:",len(fishList))