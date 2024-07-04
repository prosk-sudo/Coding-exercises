def solution(myString, pat):
    #    myString = myString.replace("A", "C")
    #    myString = myString.replace("B", "A")
    #    myString = myString.replace("C", "B")
    #
    #    return int(pat in myString)

    translation = str.maketrans("AB", "BA")
    translated_str = myString.translate(translation)

    return int(pat in translated_str)


def main():
    myString1, pat1 = "ABBAA", "AABB"
    myString2, pat2 = "ABAB", "ABAB"

    print(solution(myString1, pat1))
    print(solution(myString2, pat2))


if __name__ == "__main__":
    main()
