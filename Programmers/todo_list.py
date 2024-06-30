def solution(todo_list, finished):
    answer = []

    for i, done in enumerate(finished):
        if not done:
            answer.append(todo_list[i])
    return answer


def main():
    todo_list1, finished1 = [
        "problemsolving",
        "practiceguitar",
        "swim",
        "studygraph",
    ], [True, False, True, False]

    print(solution(todo_list1, finished1))


if __name__ == "__main__":
    main()
