import math


def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else math.prod(num_list)


def main():
    num_list_one = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
    num_list_two = [2, 3, 4, 5]

    print(solution(num_list_one))
    print(solution(num_list_two))


if __name__ == "__main__":
    main()
