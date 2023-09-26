def main():
    for a in range(1, 1000):  # a + b + c == 1000, so a < 1000
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    print(a * b * c)
                    return


if __name__ == "__main__":
    main()
