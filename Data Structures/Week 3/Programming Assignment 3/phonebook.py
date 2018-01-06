# python3


def add_number(li, number, name):
    li[number] = name


def find_number(li, number):
    if number in li.keys():
        print(li[number])
        return
    print ('not found')


def delete_number(li, number):
    if number in li.keys():
        del li[number]


def main():
    di = dict()
    n = int(input().strip())
    for i in range(n):
        query = input().strip().split()
        if query[0] == 'add':
            add_number(di, query[1], query[2])
        elif query[0] == 'find':
            find_number(di, query[1])
        else:
            delete_number(di, query[1])


if __name__ == '__main__':
    main()
