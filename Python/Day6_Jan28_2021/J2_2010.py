# CCC 2010
# Problem J2: Up and Down

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
s1 = 1*s
s2 = 1*s
sN = 0
sB = 0
while(s1>0 and s2>0):
    if a < s1:
        sN +=a
        s1 -=a
    else:
        sN +=s1
        s1 =0
    if b < s1:
        sN -=b
        s1 -=b
    else:
        sN -=s1
        s1 = 0
    if c < s2:
        sB +=c
        s2 -=c
    else:
        sB +=s2
        s2 =0
    if d < s2:
        sB -= d
        s2 -=d
    else:
        sB -=s2
        s2 =0

if sN>sB:
    print("Nikky")
elif sB>sN:
    print("Byron")
else:
    print("Tied")



