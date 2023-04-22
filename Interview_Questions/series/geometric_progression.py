def get_gp_series(x):
    series = []

    for ct, i in enumerate(range(1, x + 1)):
        sign = -1 if i % 2 == 0 else 1
        series.append(f"{sign}/{ct+i}")
    return series


for i in range(10):
    print(i, get_gp_series(i))
