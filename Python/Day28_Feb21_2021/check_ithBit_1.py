def check_i(n,i):
    if n & (1<<i):
        return True
    return False

print(check_i(7,3))