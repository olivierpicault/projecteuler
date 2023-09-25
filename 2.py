cache = {}


def fibonacci(n):
    if n in cache:
        return cache[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]


def main():
    iteration = 0
    total = 0
    result = 0

    while result < 4000000:
        result = fibonacci(iteration)
        if result % 2 == 0:
            total += result

        iteration += 1

    print(total)


if __name__ == "__main__":
    main()
