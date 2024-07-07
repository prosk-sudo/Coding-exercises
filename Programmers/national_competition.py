def solution(rank, attendance):
    lst = list((i, v) for (i, v) in enumerate(rank) if attendance[i])
    lst.sort(key=lambda x: x[1])

    return lst[0][0] * 10000 + lst[1][0] * 100 + lst[2][0]


def main():
    rank1, attendance1 = [3, 7, 2, 5, 4, 6, 1], [
        False,
        True,
        True,
        True,
        True,
        False,
        False,
    ]
    rank2, attendance2 = [1, 2, 3], [True, True, True]
    rank3, attendance3 = [6, 1, 5, 2, 3, 4], [True, False, True, False, False, True]

    print(solution(rank1, attendance1))
    print(solution(rank2, attendance2))
    print(solution(rank3, attendance3))


if __name__ == "__main__":
    main()
