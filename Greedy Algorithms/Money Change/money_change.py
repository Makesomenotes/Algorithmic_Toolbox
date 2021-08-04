# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    tens = money // 10
    money = money - tens * 10
    fives = money // 5
    money = money - fives * 5
    ones = money // 1
    return tens + fives + ones
# C:\Program Files (x86)\Python\python.exe

if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
