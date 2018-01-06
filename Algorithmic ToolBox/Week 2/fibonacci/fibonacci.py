# Uses python3
def memoize(func):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return helper

@memoize
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
