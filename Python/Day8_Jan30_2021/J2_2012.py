# CCC 2012
# Problem J2: Sounds fishy!

a,b,c,d = int(input()),int(input()),int(input()),int(input())

if a>b>c>d:
    print("Fish Diving")
elif a<b<c<d:
    print("Fish Rising")
elif a==b and b == c and c == d:
    print("Constant Depth")
else:
    print("No Fish")