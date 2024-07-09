def solution(str_list, ex):
    return "".join([s for s in str_list if ex not in s])


def main():
    str_list1, ex1 = ["abc", "def", "ghi"], "ef"
    str_list2, ex2 = ["abc", "bbc", "cbc"], "c"

    print(solution(str_list1, ex1))
    print(solution(str_list2, ex2))


if __name__ == "__main__":
    main()
