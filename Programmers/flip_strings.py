def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

def main():
    my_string_one, s_one, e_one = "Progra21Sremm3", 6, 12
    my_string_two, s_two, e_two = "Stanley1yelnatS", 4, 10

    print(solution(my_string_one, s_one, e_one))
    print(solution(my_string_two, s_two, e_two))

if __name__ == "__main__":
    main()
