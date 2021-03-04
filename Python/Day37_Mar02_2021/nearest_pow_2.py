n = int(input())

while True:
    check = n&(n-1)
    if not check:
        break
    n -=1

print(n)