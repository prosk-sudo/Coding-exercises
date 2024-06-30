def solution(arr, queries):
    for s, e in queries:
        for i in range(s, e + 1):
            arr[i] += 1
    return arr


def main():
    arr1, queries1 = [0, 1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]]

    print(solution(arr1, queries1))


if __name__ == "__main__":
    main()
