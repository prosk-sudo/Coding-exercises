def solution(arr, flag):
    answer = []
    #    for i in range(len(arr)):
    #        if flag[i]:
    #            for _ in range(arr[i]):
    #                answer.append(arr[i])
    #                answer.append(arr[i])
    #        else:
    #            for _ in range(arr[i]):
    #                answer.pop()
    for i in range(len(arr)):
        if flag[i]:
            answer.extend([arr[i]] * (2 * arr[i]))
        else:
            answer = answer[: -arr[i]]
    return answer


def main():
    arr1, flag1 = [3, 2, 4, 1, 3], [True, False, True, False, False]

    print(solution(arr1, flag1))


if __name__ == "__main__":
    main()
