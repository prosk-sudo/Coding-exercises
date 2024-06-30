def solution(num_list):
    #    even_sum = 0
    #    odd_sum = 0

    #    for i, v in enumerate(num_list):
    #        if i % 2 == 0:
    #            even_sum += v
    #        else:
    #            odd_sum += v
    #
    #    return even_sum if even_sum > odd_sum else odd_sum

    return max(sum(num_list[::2]), sum(num_list[1::2]))


def main():
    num_list1 = [4, 2, 6, 1, 7, 6]
    num_list2 = [-1, 2, 5, 6, 3]

    print(solution(num_list1))
    print(solution(num_list2))


if __name__ == "__main__":
    main()
