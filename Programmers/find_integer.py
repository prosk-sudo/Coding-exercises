def solution(num_list, n):
    #    for num in num_list:
    #        if num == n:
    #            return 1
    #    return 0

    return int(n in num_list)


def main():
    num_list1, n1 = [1, 2, 3, 4, 5], 3
    num_list2, n2 = [15, 98, 23, 2, 15], 20

    print(solution(num_list1, n1))
    print(solution(num_list2, n2))


if __name__ == "__main__":
    main()
