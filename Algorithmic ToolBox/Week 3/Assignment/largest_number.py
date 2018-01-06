#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    while a != []:
        max_digit = 0
        for digit in a:
            if checkMaximum(max_digit, digit):
                max_digit = digit
        res += str(max_digit)
        a.remove(max_digit)
    return res

def checkMaximum(m, d):
    if len(str(m)) == len(str(d)):
        return ord(str(m)) > ord(str(d))
    elif len(str(m)) > len(str(d)):
        return ord(str(m[0])) > ord(str(d[0]))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

