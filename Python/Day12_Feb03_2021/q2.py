k = 743
a = [16,1,4,2,14]
b = [7,11,2,0,15]

def countTinyPairs(a,b,k):
    count=0
    for x,y in zip(a,b[::-1]):
        con = int(str(x)+str(y))
        if con<k:
            count+=1
    return count

print(countTinyPairs(a,b,k))