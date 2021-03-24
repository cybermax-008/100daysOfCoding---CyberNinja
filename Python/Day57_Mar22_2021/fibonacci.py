# Using Recursive call
def fib(n):
    if n <= 2:
        return 1

    return fib(n-1)+fib(n-2)

# Using Recursive call with memoization
def fib_d(n,memo ={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fib_d(n-1,memo) + fib_d(n-2,memo)

    return memo[n]


print(fib(0))
print(fib(1))
# print(fib(50))

print(fib_d(0))
print(fib_d(1))
print(fib_d(7))

