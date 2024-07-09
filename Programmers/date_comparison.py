def solution(date1, date2):
    return int(date1 < date2)


def main():
    date1_1, date2_1 = [2021, 12, 28], [2021, 12, 29]
    date1_2, date2_2 = [1024, 10, 24], [1024, 10, 24]

    print(solution(date1_1, date2_1))
    print(solution(date1_2, date2_2))


if __name__ == "__main__":
    main()
