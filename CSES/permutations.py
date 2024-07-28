def main():
    answer = []
    num = int(input())
    if num == 2 or num == 3:
        print("NO SOLUTION")
    elif num == 4:
        print("2 4 1 3")
    else:
        if num % 2 == 0:
            for i in range(1, num + 1, 2):
                answer.append(i)
            for i in range(2, num + 1, 2):
                answer.append(i)
        else:
            for i in range(1, num + 1, 2):
                answer.append(i)
            for i in range(2, num + 1, 2):
                answer.append(i)
        print(''.join(str(i)+' ' for i in answer))

if __name__ == "__main__":
    main()
