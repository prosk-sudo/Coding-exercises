def main():
    answer = 0
    num = int(input())
    arr = list(map(int, input().split()))

    for i in range(num - 1):
        if arr[i] > arr[i+1]:
            answer += (arr[i] - arr[i+1])
            arr[i+1] = arr[i]
        else:
            continue

    print(answer)

if __name__ == "__main__":
    main()
