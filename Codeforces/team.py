def team(line):
    count = 0

    for i in range(line):
        a, b, c = map(int, input().split())
        if a + b + c >= 2:
            count += 1
    print(count)

    return count


def main():
    line = int(input())

    team(line)


if __name__ == "__main__":
    main()
