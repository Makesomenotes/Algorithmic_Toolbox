# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    Fib_lst = []
    for i in range(n+1):
        if i <= 1:
            Fib_lst.append(i)
        else:
            curr = Fib_lst[i-2] + Fib_lst[i-1]
            Fib_lst.append(curr)
        # print(Fib_lst[i])

    return Fib_lst[n] % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
