def toggle_ith_bit(n,i):
    return n ^ (1<<i-1)


print(toggle_ith_bit(5,1))