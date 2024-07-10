def solution(myString):
    #    answer = ""
    #    for char in myString:
    #        if char < "l":
    #            answer += "l"
    #        else:
    #            answer += char
    #    return answer

    return "".join(["l" if char < "l" else char for char in myString])


def main():
    myString1 = "abcdevwxyz"
    myString2 = "jjnnllkkmm"

    print(solution(myString1))
    print(solution(myString2))


if __name__ == "__main__":
    main()
