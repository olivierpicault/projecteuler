from functions import fibonacci


def main():
    i = 0
    while True:
        fibo = fibonacci(i)

        if len(str(fibo)) == 1000:
            print(i)
            print(fibo)
            break

        i += 1


if __name__ == "__main__":
    main()
