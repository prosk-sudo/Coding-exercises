def solution(arr):
    #    for i in range(len(arr)):
    #        if arr[i] % 2 == 0 and arr[i] >= 50:
    #            arr[i] //= 2
    #        elif arr[i] % 2 == 1 and arr[i] < 50:
    #            arr[i] *= 2
    #    return arr
    return [
        (
            num // 2
            if num % 2 == 0 and num >= 50
            else num * 2 if num % 2 == 1 and num < 50 else num
        )
        for num in arr
    ]


def main():
    arr_one = [1, 2, 3, 100, 99, 98]

    print(solution(arr_one))


if __name__ == "__main__":
    main()
