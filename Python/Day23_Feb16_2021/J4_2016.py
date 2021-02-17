# CCC 2016
# Problem J4: Arrival Time

slow1s = 7*60
slow1e = 10*60
slow2s = 15*60
slow2e = 19*60

sinput = input().split(":")
startt = int(sinput[0])*60 + int(sinput[1])

D = 240
while D > 0:
    if startt > slow1s and startt < slow1e:
        D -= 1
    elif startt > slow2s and startt < slow2e:
        D -= 1
    else:
        D -= 2
    startt += 1

if startt %10 == 9:
    startt += 1
    
s = ""
h = startt//60%24
m = startt%60

if h < 10:
    s = "0"+str(h)+":"
else:
    s = str(h) + ":"

if m < 10:
    s += "0"+str(m)
else:
    s += str(m)

print(s)
