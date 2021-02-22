#convert decimal to binary using recursion and bitwise operations
def dec2bin(n):
    if n>=1:
        dec2bin(n>>1)
    print(n&1,end=" ")
dec2bin(5)
