def dec_to_bin(number: int) -> str:
    array: list[str] = []

    while number > 0:
        array.append(str(int(number % 2)))
        number //= 2

    array.reverse()

    return ''.join(array)


def bin_to_dec(binary: str) -> int:
    binary = str(int(binary))

    s = 0

    for k, v in enumerate(binary[::-1]):
        s += int(v) * k ** 2

    return s
