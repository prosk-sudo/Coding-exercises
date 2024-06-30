def solution(arr):
    count = 0

    while True:
        arr_prev = [i for i in arr]

        for i in range(len(arr)):
            if arr[i] % 2 == 0 and arr[i] >= 50:
                arr[i] //= 2
            elif arr[i] % 2 == 1 and arr[i] < 50:
                arr[i] = arr[i] * 2 + 1
        count += 1

        if arr_prev == arr:
            break
    return count - 1


def main():
    arr_one = [1, 2, 3, 100, 99, 98]

    print(solution(arr_one))


if __name__ == "__main__":
    main()

# [3, 2, 7, 50, 49]  = arr(1)
# [7, 2, 15, 25, 99] = arr(2)
# [15, 2, 31, 51, 99] = arr(3)
# [31, 2, 63, 51, 99] = arr(4)
# [63, 2, 63, 51, 99] = arr(5)
# [63, 2, 63, 51, 99] = arr(6)
