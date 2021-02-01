
# CCC 2013
# Problem J3: From 1987 to 2013

start_year = int(input())
increment = 1
while(True):
    next_year = start_year + increment
    visited = []
    unique_flag = 0
    while(next_year>0):
        digit = next_year%10
        if digit in visited:
            unique_flag+=1
            break
        visited.append(digit)
        next_year = next_year//10
    if unique_flag==0:
        next_year = start_year + increment
        break
    increment+=1

print(next_year)



