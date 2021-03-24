def gridTraveller(m,n):
    if m==1 and n==1 :
        return 1
    if m == 0 or n ==0:
        return 0

    return gridTraveller(m-1,n) + gridTraveller(m,n-1)

def gridTraveller_d(m,n,memo={}):
    if (m,n) in memo or (n,m) in memo:
        return memo[(m,n)]
    if m==1 and n==1 :
        return 1
    if m == 0 or n ==0:
        return 0

    memo[(m,n)] = memo[(n,m)] = gridTraveller_d(m-1,n,memo) + gridTraveller_d(m,n-1,memo)

    return memo[(m,n)]

# print(gridTraveller(18,18))
print(gridTraveller_d(20,20))