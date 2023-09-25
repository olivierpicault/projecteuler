import time
import math


def is_prime(n):
    if n == 1:
        return True

    if n % 2 == 0:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def largest_prime_factor(n):
    for i in range(int(n**0.5) + 1, 1, -1):
        if n % i == 0 and is_prime(i):
            return i

    return 1


def main():
    number = 600851475143
    # number = 13195
    largest_prime = largest_prime_factor(number)
    print(largest_prime)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % round((time.time() - start_time), 5))


def test_is_prime():
    assert is_prime(1) == True
    assert is_prime(2) == False
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(17) == True
    assert is_prime(21) == False
    assert is_prime(23) == True


def test_largest_prime():
    assert largest_prime_factor(13195) == 29  # given example
