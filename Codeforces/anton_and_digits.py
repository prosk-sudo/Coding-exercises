def main():
    maximum = 0
    two, three, five, six = map(int, input().split())
    while two > 0 and five > 0 and six > 0:
        two -= 1
        five -= 1
        six -= 1
        maximum += 256

    while two > 0 and three > 0:
        two -= 1
        three -= 1
        maximum += 32

    print(maximum)


if __name__ == "__main__":
    main()
