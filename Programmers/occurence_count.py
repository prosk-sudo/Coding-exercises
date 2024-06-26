def solution(my_string):
    answer = [0] * 52
    for i in range(len(my_string)):
        if 65 <= ord(my_string[i]) <= 90:
            answer[ord(my_string[i]) - 65] += 1
        elif 97 <= ord(my_string[i]) <= 122:
            answer[ord(my_string[i]) - 97 + 26] += 1 
    return answer

def main():
    my_string_one = "Programmers"

    print(solution(my_string_one))

if __name__ == "__main__":
    main()
