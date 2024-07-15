def solution(n):
    return sum(int(digit) for digit in str(n))


def main():
    n1 = 1234
    n2 = 930211

    print(solution(n1))
    print(solution(n2))


if __name__ == "__main__":
    main()
