def set_ith_bit(n,i):
    return n | 1<<i-1

print(set_ith_bit(5,2)) # it becomes 7 -> 111
