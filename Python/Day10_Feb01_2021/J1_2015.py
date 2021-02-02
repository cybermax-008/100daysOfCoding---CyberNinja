# CCC 2015
# Problem J1: Special Day

spl_month = 2
spl_day = 18

month = int(input())
day = int(input())

if month < spl_month:
    print("Before")
elif month > spl_month:
    print("After")
else:
    if day < spl_day:
        print("Before")
    elif day > spl_day:
        print("After")
    else:
        print("Special")
