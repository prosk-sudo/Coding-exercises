def solution(arr, n):
    if len(arr) % 2 == 0:
        #        for i in range(1, len(arr), 2):
        #            arr[i] += n
        arr[1::2] = [x + n for x in arr[1::2]]
    else:
        #        for i in range(0, len(arr), 2):
        #            arr[i] += n
        arr[::2] = [x + n for x in arr[::2]]
    return arr


def main():
    arr1, n1 = [49, 12, 100, 276, 33], 27
    arr2, n2 = [444, 555, 666, 777], 100

    print(solution(arr1, n1))
    print(solution(arr2, n2))


if __name__ == "__main__":
    main()
