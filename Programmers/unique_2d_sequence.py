def solution(n):
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer


def main():
    n1 = 3
    n2 = 6
    n3 = 1

    print(solution(n1))
    print(solution(n2))
    print(solution(n3))


if __name__ == "__main__":
    main()
