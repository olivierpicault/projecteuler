from typing import List


def number_to_digits(number):
    digits = []
    while number > 0:
        last_digit = number % 10
        digits.append(last_digit)
        number = number // 10

    return digits


def sum_digits(digits: List[int]) -> int:
    return sum(digits)


def main():
    print(sum_digits(number_to_digits(2**1000)))


if __name__ == "__main__":
    main()


def test_example():
    number = 32768
    digits = number_to_digits(number)
    assert sum_digits(digits) == 26
