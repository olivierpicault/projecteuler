def number_to_digits(number):
    digits = []
    while number > 0:
        last_digit = number % 10
        digits.append(last_digit)
        number = number // 10

    return digits
