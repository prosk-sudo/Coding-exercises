def solution(picture, k):
    answer = []
    #    for row in picture:
    #        new_row = ""
    #        for char in row:
    #            new_row += char * k
    #        for _ in range(k):
    #            answer.append(new_row)

    for i in range(len(picture)):
        answer += [picture[i].replace(".", "." * k).replace("x", "x" * k)] * k
    return answer


def main():
    picture1, k1 = [
        ".xx...xx.",
        "x..x.x..x",
        "x...x...x",
        ".x.....x.",
        "..x...x..",
        "...x.x...",
        "....x....",
    ], 2
    picture2, k2 = ["x.x", ".x.", "x.x"], 3

    print(solution(picture1, k1))
    print(solution(picture2, k2))


if __name__ == "__main__":
    main()
