def solution(myString):
    #    return "".join(
    #        (
    #            char.lower()
    #            if char != "A" and char.isupper()
    #            else "A" if char == "a" else char
    #        )
    #        for char in myString
    #    )

    return myString.lower().replace("a", "A")


def main():
    myString1 = "abstract algebra"
    myString2 = "PrOgRaMmErS"

    print(solution(myString1))
    print(solution(myString2))


if __name__ == "__main__":
    main()
