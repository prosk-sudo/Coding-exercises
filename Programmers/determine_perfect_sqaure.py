def solution(n):
    return 1 if n**0.5 == int(n**0.5) else 2


def main():
    n1 = 144
    n2 = 976

    print(solution(n1))
    print(solution(n2))


if __name__ == "__main__":
    main()
