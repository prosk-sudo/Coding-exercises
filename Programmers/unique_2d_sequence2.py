def solution(arr):
    #    for i in range(len(arr)):
    #        for j in range(i + 1, len(arr)):
    #            if arr[i][j] != arr[j][i]:
    #                return 0
    #    return 1

    return int(arr == list(map(list, zip(*arr))))


def main():
    arr1 = [[5, 192, 33], [192, 72, 95], [33, 95, 999]]
    arr2 = [
        [19, 498, 258, 587],
        [63, 93, 7, 754],
        [258, 7, 1000, 723],
        [587, 754, 723, 81],
    ]

    print(solution(arr1))
    print(solution(arr2))


if __name__ == "__main__":
    main()
