# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    curr_w = 0
    curr_p = 0
    prices_per_pound = []

    for i in range(len(weights)):
        pp = prices[i] / weights[i]
        prices_per_pound.append(pp)

    while curr_w < capacity and len(weights) != 0:
        max_pp = max(prices_per_pound)
        max_index = prices_per_pound.index(max_pp)
        max_price = prices[max_index]
        max_weight = weights[max_index]
        # print(max_price, max_weight)
        test_w = curr_w + max_weight
        if test_w <= capacity:
            curr_w += max_weight
            curr_p += max_price
        else:
            res = capacity - curr_w
            curr_w += res
            curr_p += (res / max_weight) * max_price
            return curr_p
        del prices_per_pound[max_index]
        del prices[max_index]
        del weights[max_index]
    return curr_p


# 3 50 60 20 100 50 120 30
if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    #print(input_prices)
    #print(input_weights)
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
