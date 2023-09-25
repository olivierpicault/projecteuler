def is_palyndrome(number):
    tmp = number
    reversed_number = 0

    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number = number // 10

    return tmp == reversed_number


def main():
    result = 0
    for first_digit in range(99, 999):
        for second_digit in range(99, 999):
            product = first_digit * second_digit
            if is_palyndrome(product):
                result = max(result, product)

    print(result)


if __name__ == "__main__":
    main()


def test_is_palyndrome():
    assert is_palyndrome(1) == True
    assert is_palyndrome(11) == True
    assert is_palyndrome(121) == True
    assert is_palyndrome(1221) == True
    assert is_palyndrome(10) == False
    assert is_palyndrome(11001) == False
