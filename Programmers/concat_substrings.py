def solution(my_strings, parts):
#    answer = ''
#    for i, (s, e) in enumerate(parts):
#       answer += my_strings[i][s:e+1]
#    return answer

    return ''.join(my_strings[i][s:e+1] for i, (s, e) in enumerate(parts))

def main():
    my_strings_one = ["progressive", "hamburger", "hammer", "ahocorasick"]
    parts_one = [[0, 4], [1, 2], [3, 5], [7, 7]]

    print(solution(my_strings_one, parts_one))

if __name__ == "__main__":
    main()
