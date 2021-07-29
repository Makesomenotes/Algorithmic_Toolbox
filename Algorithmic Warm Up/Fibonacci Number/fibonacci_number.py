# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    Fib_lst = []
    for i in range(n+1):
        if i <= 1:
            Fib_lst.append(i)
        else:
            curr = Fib_lst[i-2] + Fib_lst[i-1]
            Fib_lst.append(curr)
        # print(Fib_lst[i])

    return Fib_lst[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
