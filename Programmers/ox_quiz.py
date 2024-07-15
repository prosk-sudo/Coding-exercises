def solution(quizzes):
    return ["O" if eval(quiz.replace("=", "==")) else "X" for quiz in quizzes]


def main():
    quiz1 = ["3 - 4 = -3", "5 + 6 = 11"]
    quiz2 = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]

    print(solution(quiz1))
    print(solution(quiz2))


if __name__ == "__main__":
    main()
