def solution(start_num, end_num):
    return [num for num in range(start_num, end_num + 1)]

def main():
    start = 3
    end = 10
    print(solution(start, end))

if __name__ == "__main__":
    main()
