def solution(arr):
    stk = []
    #    for i in range(len(arr)):
    #        if not stk:
    #            stk.append(arr[i])
    #        else:
    #            if stk[-1] == arr[i]:
    #                stk.pop()
    #            else:
    #                stk.append(arr[i])
    #    return stk if stk else [-1]

    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1]


def main():
    arr1 = [0, 1, 1, 1, 0]
    arr2 = [0, 1, 0, 1, 0]
    arr3 = [0, 1, 1, 0]

    print(solution(arr1))
    print(solution(arr2))
    print(solution(arr3))


if __name__ == "__main__":
    main()
