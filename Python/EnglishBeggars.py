def beggars(values, n):
    beggars_money = []
    for i in range(n):
        beggars_money.append(sum(values[i::n]))
    return beggars_money
