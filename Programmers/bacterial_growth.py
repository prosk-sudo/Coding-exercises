def solution(n, t):
    #    return n * (2**t)

    return n << t


def main():
    n1, t1 = 2, 10
    n2, t2 = 7, 15

    print(solution(n1, t1))
    print(solution(n2, t2))


if __name__ == "__main__":
    main()
