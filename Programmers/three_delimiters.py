#   import re


def solution(myStr):
    #    return (
    #        ["EMPTY"]
    #        if not [part for part in re.split("[abc]", myStr) if part]
    #        else [part for part in re.split("[abc]", myStr) if part]
    #    )

    answer = [
        part
        for part in myStr.replace("a", " ").replace("b", " ").replace("c", " ").split()
        if part
    ]

    return answer if answer else ["EMPTY"]


def main():
    myStr1 = "baconlettucetomato"
    myStr2 = "abcd"
    myStr3 = "cabab"

    print(solution(myStr1))
    print(solution(myStr2))
    print(solution(myStr3))


if __name__ == "__main__":
    main()
