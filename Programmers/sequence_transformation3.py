def solution(arr, k):
    #    if k % 2 == 1:
    #        for i in range(len(arr)):
    #            arr[i] *= k
    #    else:
    #        for i in range(len(arr)):
    #            arr[i] += k
    #    return arr

    return [x * k if k % 2 == 1 else x + k for x in arr]


def main():
    arr1, k1 = [1, 2, 3, 100, 99, 98], 3
    arr2, k2 = [1, 2, 3, 100, 99, 98], 2

    print(solution(arr1, k1))
    print(solution(arr2, k2))


if __name__ == "__main__":
    main()
