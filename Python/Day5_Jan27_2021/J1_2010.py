# CCC_2010
# Problem J1: What is n, Daddy? 
number = int(input())
right_hand = 5
left_hand = 5
numComb =0
for i in range(0,right_hand):
    for j in range(0,left_hand):
        if i+j == number:
            numComb+=1
        
print(numComb)