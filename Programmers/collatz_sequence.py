def solution(n):
    answer = []
    answer.append(n)

    while (n != 1):
        if n % 2 == 0:
            n //= 2
            answer.append(n)
        else:
            n = 3*n + 1
            answer.append(n)
    return answer

def main():
    n = 10
    print(solution(n))

if __name__ == "__main__":
    main()

