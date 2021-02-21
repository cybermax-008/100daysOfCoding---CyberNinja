# Count number of set bits in bit representation of a number
def count_1s(n):
    count = 0
    while(n):
        count += n & 1
        n >>=1
    return count

def count_1s_re(n):
    if n==1:
        return 1
    else:
        return n & 1 + count_1s_re(n>>1)

print(count_1s(7))
print(count_1s_re(7))