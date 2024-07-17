def solution(s):
    return "".join(sorted([char for char in s if s.count(char) == 1]))


def main():
    s1 = "abcabcadc"
    s2 = "abdc"
    s3 = "hello"

    print(solution(s1))  # "d"
    print(solution(s2))  # "abcd"
    print(solution(s3))  # "eho"


if __name__ == "__main__":
    main()
