def solution(numLog):
    answer = ''
    for i in range(len(numLog)):
        if i == 0:
            continue
        if numLog[i] - numLog[i - 1] == 1:
            answer += "w"
        elif numLog[i] - numLog[i - 1] == -1:
            answer += "s"
        elif numLog[i] - numLog[i - 1] == 10:
            answer += "d"
        else:
            answer += "a"
    return answer

def main():
    numArr = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
    print(solution(numArr))

if __name__ == "__main__":
    main()
