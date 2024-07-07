def solution(num_list):
    return sorted(num_list)[5:]


def main():
    num_list1 = [12, 4, 15, 46, 38, 1, 14, 56, 32, 10]

    print(solution(num_list1))


if __name__ == "__main__":
    main()
