# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    curr = 0
    store = 0
    stops_1 = stops.copy()
    stops_1.insert(0, 0)
    stops_1.append(d)
    n = len(stops_1)-2
    # print(stops_1)
    while curr <= n:
        last = curr
        while curr <= n:
            # print(f'New {curr}')
            if stops_1[curr + 1] - stops_1[last] <= m:
                curr += 1
            else:
                break
        if curr == last:
            return -1
        if curr <= n:
            store += 1
        # print(curr, store)
    return store


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
