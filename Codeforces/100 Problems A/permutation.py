def main():
    lst = []
    size = int(input())

    if size % 2 != 0:
        print(-1)
        return -1

    for i in range(1, size + 1):
        lst.append(i)

    for i in range(0, size, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]

    print(" ".join(map(str, lst)))


if __name__ == "__main__":
    main()
