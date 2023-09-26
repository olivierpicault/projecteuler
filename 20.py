from utils import number_to_digits


def factorial(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i

    return result


def main():
    factorial_100 = factorial(100)
    digits = number_to_digits(factorial_100)
    print(sum(digits))


if __name__ == "__main__":
    main()


def test_factorial():
    assert factorial(10) == 3628800
