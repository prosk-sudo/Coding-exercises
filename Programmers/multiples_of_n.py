def solution(n, numlist):
    return [num for num in numlist if num % n == 0]


def main():
    n1, numlist1 = 3, [4, 5, 6, 7, 8, 9, 10, 11, 12]
    n2, numlist2 = 5, [1, 9, 3, 10, 13, 5]
    n3, numlist3 = 12, [2, 100, 120, 600, 12, 12]

    print(solution(n1, numlist1))
    print(solution(n2, numlist2))
    print(solution(n3, numlist3))


if __name__ == "__main__":
    main()
