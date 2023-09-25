def is_prime(n):
    if n == 1:
        return True

    if n % 2 == 0:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def main():
    cpt = 0
    number = 0

    while cpt != 10001:
        number += 1
        if is_prime(number):
            cpt += 1

    print(number)


if __name__ == "__main__":
    main()  # brut forced, pretty fast
