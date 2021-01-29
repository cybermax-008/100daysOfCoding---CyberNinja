# CCC 2010
# Problem J3: Punchy

A = 0
B = 0

while True:
    instruction = input().split()
    # print(instruction)
    if len(instruction) == 1:
        break
    elif len(instruction) == 3:
        if int(instruction[0]) == 1:
            if instruction[1] == 'A':
                A = int(instruction[-1])
            else:
                B = int(instruction[-1])
        elif int(instruction[0]) == 3:
            if instruction[1]=='A':
                if instruction[-1] == 'B':
                    A = A+B
                else:
                    A +=A
            else:
                if instruction[-1] == 'A':
                    B = A+B
                else:
                    B +=B
        elif int(instruction[0]) == 4:
            if instruction[1]=='A':
                if instruction[-1] == 'B':
                    A = A*B
                else:
                    A *=A
            else:
                if instruction[-1] == 'A':
                    B = A*B
                else:
                    B *=B
        elif int(instruction[0]) == 5:
            if instruction[1]=='A':
                if instruction[-1] == 'B':
                    A = A-B
                else:
                    A -=A
            else:
                if instruction[-1] == 'A':
                    B = A-B
                else:
                    B -=B
        elif int(instruction[0]) == 6 :
            if instruction[1]=='A':
                if instruction[-1] == 'B':
                    A = A//B
                else:
                    A //=A
            else:
                if instruction[-1] == 'A':
                    B = A//B
                else:
                    B //=B
    else:
        if instruction[-1]=='A':
            print(A)
        else:
            print(B)