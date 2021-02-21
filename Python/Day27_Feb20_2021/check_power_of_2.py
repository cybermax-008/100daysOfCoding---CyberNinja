# check if a number is power of 2
def isPowOf2(n):
    if n==0:
        return False
    return n and not(n & (n-1))

def isPowOf2_BF(n):
    if n==0:
        return False
    while(n%2==0):
        n//=2
    return n == 1

def isPowOf2_re(n):
    if n==0:
        return False
    if n==1:
        return True
    else:
        return n%2==0 and isPowOf2_BF(n>>1)

print(isPowOf2(8))
print(isPowOf2_BF(8))
print(isPowOf2_re(8))
