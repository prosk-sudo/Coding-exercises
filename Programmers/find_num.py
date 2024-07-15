def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1


def main():
    num1, k1 = 29183, 1
    num2, k2 = 232443, 4
    num3, k3 = 123456, 7

    print(solution(num1, k1))
    print(solution(num2, k2))
    print(solution(num3, k3))


if __name__ == "__main__":
    main()
