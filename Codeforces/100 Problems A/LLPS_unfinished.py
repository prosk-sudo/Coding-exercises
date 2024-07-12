def llps(s):
    answer = ""
    max = "a"
    for i in range(len(s)):
        if s[i] > max:
            max = s[i]
    for i in range(len(s)):
        if s[i] == max:
            answer += s[i]
    return answer


def main():
    test1 = "radar"
    test2 = "bowwowwow"
    test3 = "codeforces"
    test4 = "mississipp"

    print(llps(test1))  # "rr"
    print(llps(test2))  # "wwwww"
    print(llps(test3))  # "s"
    print(llps(test4))  # "ssss"


if __name__ == "__main__":
    main()
