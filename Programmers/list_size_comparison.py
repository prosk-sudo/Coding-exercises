def solution(arr1, arr2):
    #    if len(arr1) != len(arr2):
    #        return 1 if len(arr1) > len(arr2) else -1
    #    elif len(arr1) == len(arr2) and sum(arr1) == sum(arr2):
    #        return 0
    #    else:
    #        return 1 if sum(arr1) > sum(arr2) else -1

    len1, len2 = len(arr1), len(arr2)
    sum1, sum2 = sum(arr1), sum(arr2)

    if len1 != len2:
        return 1 if len1 > len2 else -1
    if sum1 == sum2:
        return 0

    return 1 if sum1 > sum2 else -1


def main():
    arr1_1, arr1_2 = [49, 13], [70, 11, 2]
    arr2_1, arr2_2 = [100, 17, 84, 1], [55, 12, 65, 36]
    arr3_1, arr3_2 = [1, 2, 3, 4, 5], [3, 3, 3, 3, 3]

    print(solution(arr1_1, arr1_2))
    print(solution(arr2_1, arr2_2))
    print(solution(arr3_1, arr3_2))


if __name__ == "__main__":
    main()
