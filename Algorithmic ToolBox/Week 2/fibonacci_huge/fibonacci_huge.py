# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def pisano(n):
    s = []
    a = k = 0
    b = 1
    while s[:k] != s[k:] or k < 1:
        s += [a%n]
        k = len(s) // 2
        a, b = b, a + b
    return k

def fibo(n, m):
    n = n % pisano(m)
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = (arr[i - 1] + arr[i - 2]) % m
    return arr[n]

def main():
    n, m = input().split()
    n, m = int(n), int(m)
    print(fibo(n, m))

if __name__ == '__main__':
    main()