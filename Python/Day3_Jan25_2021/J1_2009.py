# Problem J1: ISBN
def check_ISBN():
    first_9digits = 9780921418
    for i in range(3):
        d = int(input())
        first_9digits = first_9digits*10 + d
    place = 0
    sum13 = 0
    # print(first_9digits)
    while(first_9digits > 0):
        last_digit = first_9digits%10
        if place%2 ==0:
            sum13+=last_digit*1
        else:
            sum13+=last_digit*3
        place+=1
        first_9digits//=10
    return sum13

print("The 1-3-sum is ",check_ISBN())
