def is_prime(n):
    # I had to change the function to make it work. It's a different one from 3.py
    if n == 1:
        return False

    if n != 2 and n % 2 == 0:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def main():
    primes_sum = 0
    for i in range(1, 2000000):
        if is_prime(i):
            primes_sum += i

    print(primes_sum)


if __name__ == "__main__":
    main()
