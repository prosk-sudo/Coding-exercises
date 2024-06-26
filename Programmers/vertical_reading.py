def solution(my_string, m, c):
#    lst = []
#    idx = 0
#
#    while (idx < len(my_string)):
#        lst.append(my_string[idx:idx+m])
#        idx += m
#
#    return ''.join(part[c-1] for part in lst)

    return my_string[c-1::m]

def main():
    my_string_one, m_one, c_one = "ihrhbakrfpndopljhygc", 4, 2
    my_string_two, m_two, c_two = "programmers", 1, 1

    print(solution(my_string_one, m_one, c_one))
    print(solution(my_string_two, m_two, c_two))

if __name__ == "__main__":
    main()
