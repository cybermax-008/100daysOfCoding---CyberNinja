# CCC 2011
# Problem J3: Sumac Sequences

t1 = int(input())
t2 = int(input())
preNum = t1
currNum = t2
count=2
while(preNum>currNum):
    temp = preNum - currNum
    preNum = currNum
    currNum = temp
    count+=1
print(count)
