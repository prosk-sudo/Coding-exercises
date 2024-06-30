def solution(names):
    return names[::5]


def main():
    names1 = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]

    print(solution(names1))


if __name__ == "__main__":
    main()
