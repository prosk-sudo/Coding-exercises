def solution(n_str):
    #    return str(int(n_str))
    return n_str.lstrip("0")


def main():
    n_str1 = "0010"
    n_str2 = "854020"

    print(solution(n_str1))
    print(solution(n_str2))


if __name__ == "__main__":
    main()
