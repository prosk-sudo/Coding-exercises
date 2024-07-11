def solution(arr):
    row_count = len(arr)
    col_count = len(arr[0])

    if row_count > col_count:
        for row in arr:
            row.extend([0] * (row_count - col_count))
    elif col_count > row_count:
        for _ in range(col_count - row_count):
            arr.append([0] * col_count)

    return arr


def main():
    arr1 = [[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]
    arr2 = [[57, 192, 534, 2], [9, 345, 192, 999]]
    arr3 = [[1, 2], [3, 4]]

    print(solution(arr1))
    print(solution(arr2))
    print(solution(arr3))


if __name__ == "__main__":
    main()
