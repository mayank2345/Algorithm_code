memo = [None] * 100


def fib(n):
    global memo
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


print(fib(10))
