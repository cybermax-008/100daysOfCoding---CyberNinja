# CCC 2011
# Problem J2: Who has Seen the Wind

h = int(input())
M = int(input())
fallen=0
for t in range(1,M):
    A = -6*t**4 + h*t**3 + 2*t**2 +t
    if A <=0:
        fallen+=1
        break
if fallen>0:
    print("The ballon first touches ground at hour:\n",t)
else:
    print("The ballon does not touch ground in the given time.")