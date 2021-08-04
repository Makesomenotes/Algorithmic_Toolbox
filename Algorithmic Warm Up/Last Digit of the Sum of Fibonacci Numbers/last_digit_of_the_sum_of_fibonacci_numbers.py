# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


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


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    return (fibonacci_number(n+2) - 1) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
