def solution(arr):
    #    answer = []
    #    for i in range(len(arr)):
    #        for _ in range(arr[i]):
    #            answer.append(arr[i])
    #    return answer

    return [num for num in arr for _ in range(num)]


def main():
    arr1 = [5, 1, 4]
    arr2 = [6, 6]
    arr3 = [1]

    print(solution(arr1))
    print(solution(arr2))
    print(solution(arr3))


if __name__ == "__main__":
    main()
