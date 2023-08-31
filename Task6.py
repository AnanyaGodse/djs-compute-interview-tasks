cube = lambda x: x ** 3


def fibonacci(n):
    if (n == 0):
        fib_list = []
    elif (n == 1):
        fib_list = [0]
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            element = fib_list[i - 1] + fib_list[i - 2]
            fib_list.append(element)

    return fib_list

n = int(input())
print(list(map(cube, fibonacci(n))))
