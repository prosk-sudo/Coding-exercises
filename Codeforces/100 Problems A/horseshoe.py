def main():
    a, b, c, d = map(int, input().split())
    my_set = set([a, b, c, d])

    print(4 - len(my_set))

    return 4 - len(my_set)


if __name__ == "__main__":
    main()
