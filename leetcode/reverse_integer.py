def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1

    x_str = str(abs(x))[::-1]
    result = sign * int(x_str)

    if result < (-2 ** 31) or result > (2 ** 31 - 1):
        return 0

    return result
