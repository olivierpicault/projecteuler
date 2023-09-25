import time


def is_divisible(number, divider):
    for i in range(1, divider + 1):
        if number % i != 0:
            return False

    return True


def smallest_number(divider):
    number = 1
    while not is_divisible(number, divider):
        number += 1

    return number


def main():
    print(smallest_number(20))  # brut forced, took 111.8 seconds, not proud of it


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % round((time.time() - start_time), 5))


def test_smaller_number():
    assert smallest_number(10) == 2520
