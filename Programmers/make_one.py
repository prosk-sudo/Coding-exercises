# import math


def solution(num_list):
    #    count = 0
    #    for i in range(len(num_list)):
    #        count += math.floor(math.log2(num_list[i]))
    #    return count

    #    return sum(len(bin(i)) - 3 for i in num_list)

    return sum(len(bin(i)[3:]) for i in num_list)


def main():
    num_list_one = [12, 4, 15, 1, 14]

    print(solution(num_list_one))


if __name__ == "__main__":
    main()
