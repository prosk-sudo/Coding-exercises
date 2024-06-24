def main():
    sum = 0
    number = int(input())
    volume_frac = map(int, input().split())

    for i in volume_frac:
        sum += i
    average = sum / number

    print(average)


if __name__ == "__main__":
    main()
