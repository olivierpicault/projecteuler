def squares_sum(n):
    result = 0
    for i in range(1, n + 1):
        result += i**2

    return result


def sum_square(n):
    result = 0
    for i in range(1, n + 1):
        result += i

    return result**2


def main():
    print(sum_square(100) - squares_sum(100))


if __name__ == "__main__":
    main()


def test_squares_sum():
    assert squares_sum(10) == 385


def test_sum_square():
    assert sum_square(10) == 3025
