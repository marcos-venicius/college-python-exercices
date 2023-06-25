from functools import reduce
# def par_entre(a: int, b:  int) -> list[int]:
#     return [i for i in range(a, b + 1) if i % 2 == 0]


# print(par_entre(0, 1_000_000))

numbers = [9.56783, 7.57568, 3.00914, 6.2321]
precision = [2, 2, 3, 3]


def rounding(x, d):
    factor = 10 ** d
    rounded_number = int(x * (factor) + 0.5 if x >= 0 else x * (factor) - 0.5)
    return rounded_number / factor


print(reduce(lambda x, y: x + y, list(map(rounding, numbers, precision))))
