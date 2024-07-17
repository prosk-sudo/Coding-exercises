def solution(my_string):
    #    return "".join(
    #        char.lower() if char.isupper() else char.upper() for char in my_string
    #    )

    return my_string.swapcase()


def main():
    my_string1 = "cccCCC"
    my_string2 = "abCdEfghIJ"

    print(solution(my_string1))
    print(solution(my_string2))


if __name__ == "__main__":
    main()
