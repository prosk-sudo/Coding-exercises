def solution(numbers):
    #    return int(
    #        numbers.replace("zero", "0")
    #        .replace("one", "1")
    #        .replace("two", "2")
    #        .replace("three", "3")
    #        .replace("four", "4")
    #        .replace("five", "5")
    #        .replace("six", "6")
    #        .replace("seven", "7")
    #        .replace("eight", "8")
    #        .replace("nine", "9")
    #    )

    for num, eng in enumerate(
        ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)


def main():
    number1 = "onetwothreefourfivesixseveneightnine"
    number2 = "onefourzerosixseven"

    print(solution(number1))
    print(solution(number2))


if __name__ == "__main__":
    main()
