my_list = ['a','b','c']
n = len(my_list)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(my_list[j],end=",")
    print()