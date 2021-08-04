# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number(n):


    Fib_lst = []
    for i in range(n+1):
        if i <= 1:
            Fib_lst.append(i)
        else:
            curr = Fib_lst[i-2] + Fib_lst[i-1]
            Fib_lst.append(curr)
        # print(Fib_lst[i])

    return Fib_lst[n]


def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

    # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    res = n % pisanoPeriod(m)
    return fibonacci_number(res) % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
